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
		irc.reply("These servers are NOT a dating service. They are a Minetest gaming system. We are here to play a game and build some cool worlds, not make out. If you want the latter, go search the web for an appropriate resource and confine your dating discussions to those places, or you WILL be removed from here. Period.")	
	dating = wrap(dating)
	def skin(self, irc, msg, args):
	    """ takes no arguments
	    Displays how to get a skin on a Minetest server, if the server supports it.
	    """
	    irc.reply("To get a skin, send a link to the skin you want to the server's Owner. Once installed, it will take effect at the next restart (usually around 10:00 AM UTC/5:00 AM EST). Minetest uses the same skin format as Minecraft, just search the web or go to minecraftskins.com or similar. A skin works only on the server it was installed on.")
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
		irc.reply("We expect users on our servers to treat each other with respect. That means not cussing people out, telling people to shut up , etc. You were not taught by your parents to act any other way, and we expect you to behave appropriately to be here. Treat others as you'd want to be treated. If you can't abide by this simple rule, then leave or you will be removed.")
	respect = wrap(respect)
Class = Minetest_Rules


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
