# coding=utf-8
from __future__ import absolute_import

__author__ = "Jarek Szczepanski <imrahil@imrahil.com>"
__license__ = "GNU Affero General Public License http://www.gnu.org/licenses/agpl.html"
__copyright__ = "Copyright (C) 2014 Jarek Szczepanski - Released under terms of the AGPLv3 License"

import octoprint.plugin

class NavBarPlugin(octoprint.plugin.TemplatePlugin, octoprint.plugin.AssetPlugin):
            
    ##~~ AssetPlugin API
    
    def get_assets(self):
        return {
            "js": ["js/navbartemp.js"],
            "css": ["css/navbartemp.css"],
            "less": ["less/navbartemp.less"]
        } 
        
__plugin_name__ = "Navbar Temperature Plugin"
__plugin_implementations__ = [NavBarPlugin()]
