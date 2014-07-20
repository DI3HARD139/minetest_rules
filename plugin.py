###
# Copyright (c) 2014, Nicholas De Nova
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.ircmsgs as ircmsgs
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Minetest_Rules')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

class Minetest_Rules(callbacks.Plugin):
	"""Add the help for "@plugin help Minetest_Rules" here
	This should describe *how* to use this plugin."""
	pass
	
	def dating(self, irc, msg, args):
		""" takes no arguments
		For Minetest rules output.
		"""
		irc.reply("These servers are NOT a dating service. They are a Minetest gaming system. We are here to play a game and build some cool worlds, not make out. If you want the latter, go search the web for an appropriate resource and confine your dating discussions to those places, or you WILL be removed from here. Period.", prefixNick = False)	
	dating = wrap(dating)
	def skin(self, irc, msg, args):
	    """ takes no arguments
	    Displays how to get a skin on a Minetest server, if the server supports it.
	    """
	    irc.reply("To get a skin, send a link to the skin you want to the server's Owner. Once installed, it will take effect at the next restart (usually around 10:00 AM UTC/5:00 AM EST). Minetest uses the same skin format as Minecraft, just search the web or go to minecraftskins.com or similar. A skin works only on the server it was installed on.", prefixNick = False)
	skin = wrap(skin)
	
	# Alias for "skin"
	def skins(self, irc, msg, args):
		""" takes no arguments
		Displays how to get a skin on a Minetest server, if the server supports it.
		"""
		Minetest_Rules.skin(self, irc, msg, args)
	skins = wrap(skins)
	
	def respect(self, irc, msg, args):
		""" takes no arguments
		Tells a user about respect.
		"""
		irc.reply("We expect users on our servers to treat each other with respect. That means not cussing people out, telling people to shut up , etc. You were not taught by your parents to act any other way, and we expect you to behave appropriately to be here. Treat others as you'd want to be treated. If you can't abide by this simple rule, then leave or you will be removed.", prefixNick = False)
	respect = wrap(respect)
	
	def rules(self, irc, msg, args):
		""" takes no arguments
		Tells people how to find the rules.
		"""
		irc.reply("On every server is a set of rules. In order to build and dig on that server, you must first seek out and read the rules. These are usually found near the spawn building. Then, depending on the server, you may need to present a code to verify that you have read the rules.", prefixNick = False)
	rules = wrap(rules)
	
	def spawn(self, irc, msg, args):
		""" takes no arguments
		Tells people how to use the /spawn command.
		"""
		irc.reply("Most servers have a \"/spawn\" command, that will return you to your starting point. This is especially useful if you need to meet other players, or if you need to get unstuck. To use it, simply type \"/spawn\" into chat.", prefixNick = False)
	rules = wrap(rules)
	
	def  worldcraft(self, irc, msg, args):
		""" takes no arguments
		Tells people about the illegal tablet clients that are frequently used.
		"""
		irc.reply("Worldcraft, Buildcraft, Starve Games and others are unsupported versions of Minetest. You will most likely experience poor performance, low framerate or lag. Either get Minetest for a PC, or, if a tablet is your only option, get it from the Minetest forums (https://forum.minetest.net/viewtopic.php?f=42&t=9389). ", prefixNick = False)
	worldcraft = wrap(worldcraft)
	
	def buildcraft(self, irc, msg, args):
		""" takes no arguments
		Tells people about the illegal tablet clients that are frequently used.
		"""
		Minetest_Rules.worldcraft(self, irc, msg, args)
	buildcraft = wrap(buildcraft)
	
	def lag(self, irc, msg, args):
		""" takes no arguments
		Tells people about the differences between lag and low FPS.
		"""
		irc.reply("Lag is not low FPS. Low FPS makes the game appear slow and glitchy. Lag makes opening chests and doors take a bit of time.", prefixNick = False)
	lag = wrap(lag)
	
	def protect(self, irc, msg, args):
		""" takes no arguments
		Tells people how to properly protect their land.
		"""
		irc.reply("To protect your land, go to one corner of the area, dig into the ground, and type \"/area_pos1\" without quotes. Then, go to the other corner and build into the sky, then type \"/area_pos2\", again, without quotes. After you finish doing that, type \"/protect <your_area_description>\" without quotes (fill in your description instead of <your_area_description>). Your land is now protected! Please note that only protecting rectangles of land are supported.", prefixNick = False)
	protect = wrap(protect)
	
	def asking(self, irc, msg, args):
		""" takes no arguments
		Tells people how to ask a question.
		"""
		irc.reply("Do not just scream \"HELP!\" in chat. If you need something done, say <username>, <your question>. For instance, if you need help with building, say \"sample_dude, I need help building.\".", prefixNick = False)
	asking = wrap(asking)
	
	def language(self, irc, msg, args):
		""" takes no arguments
		Warns users about foul language.
		"""
		irc.reply("This is a family friendly network. This means no foul language in chat. If you do need to curse, please blur it sufficiently (wtf, and s*** are acceptable). If you do swear in chat, you will be asked, then eventually forced to stop. This is considered a major offense and may end in a ban.", prefixNick = False)
	language = wrap(language)
	
	def interact(self, irc, msg, args):
		""" takes no arguments
		Tells users how to get interact.
		"""
		irc.reply("Interact allows you to build and dig on the servers. Most servers do not have interact by default. You must read the rules and understand them fully, then ask a moderator for interact in chat. If one does not respond immediately, please wait until one of the moderators listed at the rules responds. Meanwhile, you may walk around the servers and take advantage of the view.", prefixNick = False)
	interact = wrap(interact)
	
	def mtzbskins(self, irc, msg, args):
		""" takes no arguments
		Tells users how to get skins on Onez's Minetest Server.
		"""
		irc.reply("To get a skin on Onez's server, email the link to the skin's raw image to mtz_deezl@yahoo.com, or, if you can, paste the link to the raw image in chat. Use a site such as www.minecraftskins.com. Only Zeno`/onez and deezl can apply skins. Please say their name to alert them that you would like a skin. Please note that the skin will not be applied until the next server restart.", prefixNick = False)
	mtzbskins = wrap(mtzbskins)
	
	def irc(self, irc, msg, args):
		""" takes no arguments
		Tells users how to use the IRC server.
		"""
		irc.reply("The chat on these servers is interlinked through an IRC network. IRC is an acronym for \"Internet Relay Chat\". Please note that IRC is /not/ a game. If you would like to join IRC, use a web client such as KiwiIRC ( www.kiwiirc.com ), or a downloadable client such as HexChat for PC, or an app such as MangoIRC for tablets.", prefixNick = False)
	irc = wrap(irc)
	
	def chatinterlink(self, irc, msg, args):
		""" takes no arguments
		Explains how the chat is interlinked between servers.
		"""
		irc.reply("If you cannot see players, then they are most likely on another server. (The easiest way to tell is if they have an \"@\" symbol after their name.) The reason that you can still hear them talking in chat is that they are connected with an internet chat protcol called IRC.", prefixNick = False)
	chatinterlink = wrap(chatinterlink)
	
	def usingcommands(self, irc, msg, args):
		""" takes no arguments
		Explains to users how to use chat commands.
		"""
		irc.reply("To use chat commands, first type a forward slash  /   and then the name of the command. For instance, if you are trying to use the \"spawn\" command, type it in without any spaces or extra words. Like such: /spawn", prefixNick = False)
	usingcommands = wrap(usingcommands)
	
	def caps(self, irc, msg, args):
		""" takes no arguments
		Tells users not to shout.
		"""
		irc.reply("Please do not talk in ALL CAPS. This is considered shouting, and is against the rules. If you continue to talk in caps, you will be kicked, then eventually banned.", prefixNick = False)
	caps = wrap(caps)
	
	def shouting(self, irc, msg, args):
		""" takes no arguments
		Tells users not to shout.
		"""
		caps(self, irc, msg, args)
	shouting = wrap(shouting)
	
	def flooding(self, irc, msg, args):
		""" takes no arguments
		Tells users about flooding.
		"""
		irc.reply("Do not flood. Flooding is saying large amounts of gibberish or nonsense for no reason. Doing this may result in a kick or ban.",prefixNick = False)
	flooding = wrap(flooding)
	
	def spam(self, irc, msg, args):
		""" takes no arguments
		Tells users about spamming.
		"""
		irc.reply("Do not spam. Spamming is saying things in a deliberate attempt to lead people away from the conversation, or to advertise a product. Doing this may result in a kick or ban.", prefixNick = False)
	spam = wrap(spam)
	
	def teleport(self, irc, msg, args):
		""" takes no arguments
		Tells users about teleporting.
		"""
		irc.reply("This is Minetest, not Minecraft. Commands such as \"\\tp\" and \"tp\\username\" will not work. Teleporting requires a privilege, and it is only given to admins and moderators.", prefixNick = False)
	teleport = wrap(teleport)
	
	def privileges(self, irc, msg, args):
		""" takes no arguments
		Tells users about the Minetest privilege system.
		"""
		irc.reply("Minetest privileges are a way of allowing users to do certain things, for instance, there is a \"fast\" priv that allows you to move quickly. Please do not ask for extra privs; they will not be granted.", prefixNick = False)
	privileges = wrap(privileges)
Class = Minetest_Rules


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
