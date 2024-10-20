

queryOwningTournamentsInfo = """
{
  me {
    ownTournaments {
        name
        state,
        schedule {
          scheduledStartTimeAt
        }
        
    }
  }

}
"""

queryAllTournamentsInfo = """
{
  tournamentsForSpace(
    input: {
        spaceId: "d8dcfecd-3f98-40cd-47ec-08d93be39384",
        tournamentFilter: { openTournamentSelector: {excludeRunning: false} },
        gameSettingFilters: []
    }
  
  ) 
  
  {
    name
    state,
    schedule {
      scheduledStartTimeAt
    }
  }

}
"""

queryPersonalInfo = """
{
  me {
    user {
        username,
        biography,
        profileUrl
    }
  }

}
"""