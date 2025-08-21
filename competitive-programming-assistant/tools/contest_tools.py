from datetime import datetime
from typing import Annotated, List, Optional

from pydantic import Field
from mcp import ErrorData, McpError

from api_clients.clist import CListAPI
from tools.models import RichToolDescription
from mcp_instance import mcp

# --- TOOL: Get Upcoming Contests ---
UpcomingContestsDesc = RichToolDescription(
    description="Gets a list of upcoming and running contests from major platforms with names, times, duration, and links.",
    use_when="User wants to plan contest participation, check schedules, or uses phrases like 'upcoming contests', 'contest schedule', 'what contests are coming', 'when is next contest', 'contest calendar', 'running contests', 'live contests', 'contest list', or 'what's next on [platform]'.",
    side_effects="Makes network requests to the clist.by API which aggregates contest data from multiple platforms. Response time typically 2-4 seconds depending on number of platforms requested."
)

@mcp.tool(description=UpcomingContestsDesc.model_dump_json())
async def get_upcoming_contests(
    platforms: Annotated[Optional[List[str]], Field(description="Platforms to check. Supported: codeforces, leetcode, codechef, atcoder, topcoder, codingninjas.")] = None,
    limit: Annotated[int, Field(description="Maximum number of contests to return.")] = 10
) -> str:
    target_platforms = platforms or ["codeforces", "leetcode", "codechef"]
    try:
        contests = await CListAPI.get_upcoming_contests(target_platforms)
        if not contests:
            return f"😕 No upcoming contests found for: {', '.join(target_platforms)}."

        response = f"📅 **Upcoming Contests ({', '.join(target_platforms).title()})**\n\n"
        for contest in contests[:limit]:
            start_dt = datetime.fromisoformat(contest['start'].replace('Z', '+00:00'))
            end_dt = datetime.fromisoformat(contest['end'].replace('Z', '+00:00'))
            response += f"- **{contest['event']}**\n"
            response += f"  - **On:** {contest['resource']}\n"
            response += f"  - **Starts:** {start_dt.strftime('%a, %b %d @ %I:%M %p %Z')}\n"
            response += f"  - **Duration:** {str(end_dt - start_dt)}\n"
            response += f"  - **Link:** [View Contest]({contest['href']})\n---\n"
        return response.strip()
    except Exception as e:
        raise McpError(ErrorData(code=500, message=f"❌ Error fetching upcoming contests: {str(e)}"))