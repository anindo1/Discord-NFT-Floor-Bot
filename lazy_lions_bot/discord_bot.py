import discord
from bot_commands import *

# design messages to look better: https://discordjs.guide/popular-topics/embeds.html#embed-preview

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!commands"):
        embed = discord.Embed(title="Commands for Lazy Lions Bot", color=0xE50B0B)
        embed.set_thumbnail(
            url="https://lh3.googleusercontent.com/BvipQ9y_NwPvBHYiU0SBRB5Eu2pydp7Gm6i6tSpMQWwt7pr9vDc14wBYTdxwoFPTkySGEx5Ne__zJ3t70mKSz_bPfAb4gE1ZCTDQbac=s2500"
        )
        embed.add_field(name="Check All Stats", value="!stats", inline=False)
        embed.add_field(name="Check Floor Price", value="!floor", inline=True)
        embed.add_field(
            name="Check Floor Price on Specific Trait",
            value="!floor <trait type> <trait>",
            inline=False,
        )
        embed.add_field(name="Example", value="!floor body scratched up", inline=True)
        embed.add_field(
            name="Check Total Volume (in Eth)", value="!volume", inline=False
        )
        embed.add_field(
            name="Check Number of Total Unique Owners", value="!owners", inline=False
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!stats"):
        response = mainStats("stats")
        embed = embededMessage("Stats", response)
        await message.channel.send(embed=embed)

    if message.content.startswith("!floor"):
        if len(message.content) > 7:
            split_message = message.content.split()
            trait_type = split_message[1].capitalize()
            trait = split_message[2].capitalize()
            urlTrait = trait
            counter = 3
            while counter < len(split_message):
                urlTrait = urlTrait + "%20" + split_message[counter].capitalize()
                trait = trait + " " + split_message[counter].capitalize()
                counter += 1
            response = traitFloor(trait_type, urlTrait)

            if type(response) is str:
                await message.channel.send(response)
            else:
                embed = embededMessage("Floor Price for " + trait, response)
                await message.channel.send(embed=embed)
        else:
            response = mainStats("floor")
            embed = embededMessage("Floor Price", response)
            await message.channel.send(embed=embed)

    if message.content.startswith("!volume"):
        response = mainStats("volume")
        embed = embededMessage("Total Volume", response)
        await message.channel.send(embed=embed)

    if message.content.startswith("!owners"):
        response = mainStats("num_owners")
        embed = embededMessage("Number of Owners", response)
        await message.channel.send(embed=embed)


def embededMessage(name, data):
    embed = discord.Embed(
        title="Stats for Lazy Lions",
        url=data[0],
        description="Click to view on opensea",
        color=0xE50B0B,
    )
    embed.set_thumbnail(
        url="https://lh3.googleusercontent.com/BvipQ9y_NwPvBHYiU0SBRB5Eu2pydp7Gm6i6tSpMQWwt7pr9vDc14wBYTdxwoFPTkySGEx5Ne__zJ3t70mKSz_bPfAb4gE1ZCTDQbac=s2500"
    )
    if len(data) == 2:
        embed.add_field(name=name, value=data[1], inline=False)
    else:
        embed.add_field(name="Floor Price", value=data[17], inline=False)
        embed.add_field(name="Number of Owners", value=data[15], inline=False)
        embed.add_field(name="Average Price", value=data[16], inline=False)
        embed.add_field(name="Total Sales", value=data[14], inline=False)
        embed.add_field(name="Total Volume", value=data[13], inline=False)
        embed.add_field(name="30 Day Average Price", value=data[12], inline=False)
        embed.add_field(name="30 Day Sales", value=data[11], inline=False)
        embed.add_field(name="30 Day Change", value=data[10], inline=False)
        embed.add_field(name="30 Day Volume", value=data[9], inline=False)
        embed.add_field(name="7 Day Average Price", value=data[8], inline=False)
        embed.add_field(name="7 Day Sales", value=data[7], inline=False)
        embed.add_field(name="7 Day Change", value=data[6], inline=False)
        embed.add_field(name="7 Day Volume", value=data[5], inline=False)
        embed.add_field(name="1 Day Average Price", value=data[4], inline=False)
        embed.add_field(name="1 Day Sales", value=data[3], inline=False)
        embed.add_field(name="1 Day Change", value=data[2], inline=False)
        embed.add_field(name="1 Day Volume", value=data[1], inline=False)

    return embed


client.run("ODc2NzA5NjQxOTkwNTkwNDY0.YRoBew.FQJWCUuA4n1syvtUeaXf3vvNiX8")
