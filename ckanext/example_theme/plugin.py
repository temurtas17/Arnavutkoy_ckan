import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.common import CKANConfig
from flask import Blueprint
from ckanext.example_theme.controller import MyLogic


# import ckanext.example_theme.cli as cli
# import ckanext.example_theme.helpers as helpers
# import ckanext.example_theme.views as views
# from ckanext.example_theme.logic import (
#     action, auth, validators
# )

def my_package_show(id):
    context = {'ignore_auth': True}
    data_dict = {'id': id, 'include_tracking': True}  # İsteğe bağlı: veri filtreleme vb. için kullanılabilir
    # CKAN'in package_show fonksiyonunu çağırın
    package = toolkit.get_action('package_show')(context, data_dict)

    # package içindeki tracking_summary bilgisini alın
    tracking_summary = package.get('tracking_summary')

    # tracking_summary'i kullanarak istediğiniz işlemleri yapın
    # Örnek olarak, tracking_summary'yi bir değişkene atayabilirsiniz
    my_variable = tracking_summary['total']

    # Sonucu döndürün
    return my_variable

def most_popular_datasets():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    context = {'ignore_auth': True}
    data_dict = {}  # İsteğe bağlı: veri filtreleme vb. için kullanılabilir
    datasets = toolkit.get_action('current_package_list_with_resources')(context, data_dict)
    # Truncate the list to the 10 most popular groups only.
    datasets = datasets[:6]

    return datasets

class ExampleThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    

    # IConfigurer

    def update_config(self, config: CKANConfig):
        toolkit.add_template_directory(config, "templates")
        toolkit.add_public_directory(config, "public")
        toolkit.add_resource("assets", "example_theme")

    def get_blueprint(self):
        blueprint = Blueprint(self.name, self.__module__)

        blueprint.add_url_rule(
            u'/iletisim',
            u'do_something',
            MyLogic.do_something,
            methods=['GET']
        )

        blueprint.add_url_rule(
            u'/acikveri',
            u'show_acikveri',
            MyLogic.show_acikveri,
            methods=['GET']
        )
        
        return blueprint

    
    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    def get_helpers(self):
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'example_theme_most_popular_datasets': most_popular_datasets,
                'example_theme_my_package_show': my_package_show}

    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()
    
