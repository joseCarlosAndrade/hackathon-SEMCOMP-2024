query1 = """
{
  me {
    user {
        username,
        biography
    }

    ownTournaments {
        name
        matchSeries {
            title
            state
            matches {
                state
                }
        }
    }
  }

}
"""

query2 = """
{
  me {
    ownTournaments {
        name
        description
        schedule {
            scheduledStartTimeAt,
            confirmationWindowOpenAt,
            earlyConfirmationWindowOpenAt,
            allowEarlyConfirmation,
            startedAt,
            endedAt
        }
    }
  }

}
"""

query3 = """
{
  me {
    ownTournaments {
        name
        schedule {
            scheduledStartTimeAt,
            confirmationWindowOpenAt,
            earlyConfirmationWindowOpenAt,
            allowEarlyConfirmation,
            startedAt,
            endedAt
        }
    }
  }

}
"""

query4 = """
{
  me {
    matchmaking {
        joinedQueue {
            waitingCount
        }
    }
  }

}
"""

query5 = """
{
  me {
    matchmaking {
        offers {
            participantCount
        }
    }
  }

}
"""

query6 = """
{
  me {
    ownTournaments {
        hosts {
            spaces {
                name,
                id
            }
        }
    }
  }

}
"""

query7 = """
{
  tournamentsForSpace(
    input: {
        spaceId: "d8dcfecd-3f98-40cd-47ec-08d93be39384",
        tournamentFilter: { openTournamentSelector: {excludeRunning: false} },
        gameSettingFilters: []
    }
  
  ) {
    name
  }

}
"""