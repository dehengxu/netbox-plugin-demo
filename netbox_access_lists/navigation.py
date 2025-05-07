from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from netbox.choices import ButtonColorChoices
from netbox.plugins.utils import get_plugin_config

menu_name = get_plugin_config("netbox_dns", "menu_name")
top_level_menu = get_plugin_config("netbox_dns", "top_level_menu")

accesslist_buttons = [
    PluginMenuButton(
        link='plugins:netbox_access_lists:accesslist_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

accesslistrule_butons = [
    PluginMenuButton(
        link='plugins:netbox_access_lists:accesslistrule_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

_menu_items = (
    PluginMenuItem(
        link='plugins:netbox_access_lists:accesslist_list',
        link_text='Access Lists',
        buttons=accesslist_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_access_lists:accesslistrule_list',
        link_text='Access List Rules',
        buttons=accesslistrule_butons
    ),
)

if top_level_menu:
  menu = PluginMenu(
      label="Access Lists",
      groups=(("AccessLists", _menu_items),),
      icon_class="mdi mdi-domain",
  )
else:
  menu_items = _menu_items