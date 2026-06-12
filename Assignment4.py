# Assignment 3: Real world application of loop control statements
# A program that simulates a country that will win World Cup 2026
# Using while loop, break, continue, and pass statements

import random

teams = [
    "Uganda", "Brazil", "France", "Argentina",
    "England", "Germany", "Spain", "Portugal",
    "Morocco", "USA", "Japan", "Nigeria"
]

print("=" * 50)
print("   ⚽ FIFA WORLD CUP 2026 SIMULATOR ⚽")
print("=" * 50)

player_name = input("Enter your name: ")
country = input("Enter your country to support: ").strip()

if country not in teams:
    teams.append(country)
    print(f"✅ {country} added to the tournament!")

print(f"\nWelcome {player_name}! Supporting {country} 🏳️")
print(f"\nTournament begins with {len(teams)} teams!\n")

# ---- WHILE LOOP controls the entire game flow ----
while len(teams) > 1:

    print("""
==============================
        MENU
==============================
1. Simulate next match
2. View remaining teams
3. Skip this round
4. Exit tournament
==============================""")

    choice = input("Enter choice (1-4): ").strip()

    # ---- BREAK: Exit the loop early ----
    if choice == "4":
        print(f"\n🚪 You exited the tournament early!")
        print(f"Remaining teams: {', '.join(teams)}")
        break

    # ---- CONTINUE: Skip back to top of loop ----
    elif choice == "3":
        print("\n⏭️ Skipping this round...")
        continue

    # ---- PASS: Placeholder, do nothing ----
    elif choice == "2":
        print("\n🏆 Remaining teams:")
        for i, team in enumerate(teams, 1):
            print(f"  {i}. {team}")
        pass  # pass used here — no action needed, loop continues naturally

    # ---- Simulate a match ----
    elif choice == "1":
        if len(teams) < 2:
            break

        # Pick two random teams
        team1, team2 = random.sample(teams, 2)
        winner = random.choice([team1, team2])
        loser = team2 if winner == team1 else team1

        print(f"\n⚽ MATCH: {team1}  vs  {team2}")
        print(f"🏆 WINNER: {winner}")
        print(f"❌ ELIMINATED: {loser}")

        # Remove loser from tournament
        teams.remove(loser)

        # Check if supported country got eliminated
        if loser == country:
            print(f"\n😢 Oh no! {country} has been eliminated from the World Cup!")
            print("You can continue watching other matches.")

        # Check if supported country won the match
        elif winner == country:
            print(f"\n🎉 {country} won this match! Keep going!")

    else:
        print("❌ Invalid choice! Enter 1-4.")
        continue

    # ---- Check if tournament is over ----
    if len(teams) == 1:
        champion = teams[0]
        print(f"""
🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊
  ⚽ WORLD CUP 2026 CHAMPION ⚽
        {champion} 🏆
🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊""")

        if champion == country:
            print(f"\n🥳 CONGRATULATIONS {player_name}!")
            print(f"{country} WON THE WORLD CUP 2026! 🏆🎉")
        else:
            print(f"\n😢 Sorry {player_name}, {country} didn't win this time.")
            print(f"{champion} takes the trophy!")
        break