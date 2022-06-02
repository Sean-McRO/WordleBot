import discord
from discord.ext import commands
import game_logic

# icon output
correct = "green_square"
partial = "yellow_square"
incorrect = ":red_square:"
blank = ":white_square_button:"

client = commands.Bot(commands_prefix="w!")


@commands.command()
async def play_game(ctx):
    await ctx.send("Enter Word Length:")
    message_response = client.wait_for("message", check=lambda m: m.user == ctx.user)
    answer = game_logic.get_word(message_response.content)[0]

    i = 0
    slots = []
    while i < len(answer) + 1: slots.append(blank); i = i + 1
    await ctx.send("[[" + ''.join(slots) + "]]")

    guesses = 0
    while guesses < 6:
        results = run_input(ctx, slots, answer)
        if results[1] == "correct":
            ctx.send("correct, the answer was %s" % results[2])
            break
        # above is probably not correct, is a while loop even the right choice?
        guesses = guesses + 1


def run_input(ctx, slots, answer):
    # have I correctly called for user input?
    message_response = client.wait_for("message", check=lambda m: m.user == ctx.user)
    game_logic.sanitize("str", len(answer) + 1, 0, 0, answer)
    answers_compared = game_logic.compare_answer(answer, message_response.content)
    correct_letters = answers_compared[0]
    correct_places = answers_compared[1]
    status = "incomplete"
    for i in slots:
        slots[i] = incorrect
    for i in correct_letters:
        slots[i] = partial
    for i in correct_places:
        slots[i] = correct
    # if the number of correct slots is the same as the number of slots game is won
    if slots.count(correct):
        status = "complete"
    return slots, status, message_response.content
