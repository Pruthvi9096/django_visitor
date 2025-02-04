

import os
import csv


class ModuleBuilder:
   

    def __init__(self, module_name, path_to_csv, path_to_save):
       
        self.module_name = module_name
        self.path_to_csv = path_to_csv
        self.path_to_save = path_to_save + "/"
        self.import_model = [
            "from odoo import fields",
            "from odoo import models",
            "from odoo import api",
        ]
       
        self.disabled_generate_field = [
            "tree", "form", "model", "type", "field"
        ]

        self.create_module()

    def check_dir(self, path):
        if not os.path.isdir(path):
            os.makedirs(path)

    def get_dict_from_csv(self):
        with open(self.path_to_csv) as file:
            reader = csv.DictReader(file)
            result = {}
            for row in reader:
                try:
                    result[row["model"]].append(row)
                except:
                    result[row["model"]] = [row]

            return result

    def to_camelcase(self, name):
        return name.replace(".", " ").title().replace(" ", "")

    def create_module(self):
        dict_from_csv = self.get_dict_from_csv()
        model_path = self.path_to_save + "models/"
        view_path = self.path_to_save + "views/"
        self.check_dir(self.path_to_save)
        self.check_dir(model_path)
        self.check_dir(view_path)
        manifest = []

        for key, value in dict_from_csv.items():
            self.create_model(model_path, key, value)
            self.create_view(view_path, key, value)

            manifest.append(key.lower().replace(".", "_"))

        self.create_view_menu(view_path, manifest)
        self.create_init_python(model_path, manifest)
        self.create_manifest(manifest)

    def create_model(self, model_path, key, value):
   
        filename = key.lower().replace(".", "_") + ".py"
        path_to_file = model_path + filename

        with open(path_to_file, "w") as file:
            file.write('# -*- coding: utf-8 -*-\n')
            file.write('\n'.join(self.import_model))
            file.write('\n\n\nclass {}(models.Model):'.format(
                self.to_camelcase(key)))
            file.write('\n\t_name = "{}"\n'.format(key))
            for field in value:
                file.write(self.generate_field(field))

    def generate_field(self, field):
        result = '\n\t{} = fields.{}('.format(
            field["field"], field["type"].capitalize())
        for key, value in field.items():
            if value and value.title() != "False" and key.lower() not in self.disabled_generate_field:
                result += '{}="{}", '.format(key, value.title() if key not in [
                                             "comodel_name", "inverse_name"] else value.lower())
        result = result[:-2]
        result += ')'

        return result

    def create_view(self, view_path, key, value):
        filename = key.lower().replace(".", "_") + ".xml"
        path_to_file = view_path + filename

        with open(path_to_file, "w") as file:
            file.write('<?xml version="1.0" encoding="utf-8"?>\n<odoo>')
            self.create_view_tree(file, key, value)
            self.create_view_form(file, key, value)
            self.create_view_action(file, key)
            file.write('\n</odoo>')

    def create_view_tree(self, file, key, value):
        file.write('\n<record id="{}" model="ir.ui.view">'.format(
            key.lower().replace(".", "_") + '_tree'))
        file.write('\n\t<field name="name">{}</field>'.format(key+'.view.tree'))
        file.write('\n\t<field name="model">{}</field>'.format(key))
        file.write('\n\t<field name="arch" type="xml">')
        file.write('\n\t\t<tree>')
        for field in value:
            if field["tree"].title() != "False" or not field["tree"]:
                file.write('\n\t\t\t<field name="{}"/>'.format(field["field"]))
        file.write('\n\t\t</tree>')
        file.write('\n\t</field>')
        file.write('\n</record>\n\n')

    def create_view_form(self, file, key, value):
        file.write('<record id="{}" model="ir.ui.view">'.format(
            key.lower().replace(".", "_") + '_form'))
        file.write('\n\t<field name="name">{}</field>'.format(key+'.view.form'))
        file.write('\n\t<field name="model">{}</field>'.format(key))
        file.write('\n\t<field name="arch" type="xml">')
        file.write('\n\t\t<form>')
        file.write('\n\t\t\t<sheet>')
        file.write('\n\t\t\t\t<group>')
        for field in value:
            if field["form"].title() != "False" or not field["form"]:
                file.write(
                    '\n\t\t\t\t\t<field name="{}"/>'.format(field["field"]))
        file.write('\n\t\t\t\t</group>')
        file.write('\n\t\t\t</sheet>')
        file.write('\n\t\t</form>')
        file.write('\n\t</field>')
        file.write('\n</record>\n\n')

    def create_view_action(self, file, key):
        file.write('<record id="{}" model="ir.actions.act_window">'.format(
            key.lower().replace(".", "_") + '_action'))
        file.write(
            '\n\t<field name="name">{}</field>'.format(key.lower().replace(".", " ").title() + ' Action'))
        file.write('\n\t<field name="type">ir.actions.act_window</field>')
        file.write('\n\t<field name="res_model">{}</field>'.format(key))
        file.write('\n\t<field name="view_mode">tree,form</field>')
        file.write('\n</record>')

    def create_view_menu(self, view_path, manifest):
        menu_base = self.module_name.replace(" ", "_").lower() + "_base_menu"
        path_to_file = view_path + "menu.xml"
        with open(path_to_file, "w") as file:
            file.write('<?xml version="1.0" encoding="utf-8"?>')
            file.write('\n<odoo>')
            file.write(
                '\n\t<menuitem name="{}" id="{}"/>'.format(self.module_name, menu_base))
            for menu in manifest:
                file.write('\n\t<menuitem name="{}" id="{}" parent="{}" action="{}"/>'.format(
                    menu.replace("_", " ").title(), menu, menu_base, menu + "_action"))
            file.write('\n</odoo>')

    def create_init_python(self, model_path, manifest):
        with open(self.path_to_save + "__init__.py", "w") as file:
            file.write("from . import models")

        with open(model_path + "__init__.py", "w") as file:
            for model in manifest:
                file.write('from . import {}\n'.format(model))

    def create_manifest(self, manifest):
        with open(self.path_to_save + "__manifest__.py", "w") as file:
            file.write('{')
            file.write('\n\t"name": "{}",'.format(self.module_name))
            file.write('\n\t"version": "1.0",')
            file.write('\n\t"author": "Andre Agung Purnomo",')
            file.write('\n\t"summary": "Place your summary in here",')
            file.write(
                '\n\t"description": "Place your description in here. Feel free to contact me +6287731588137",')
            file.write('\n\t"data": [')
            for view in manifest:
                file.write('\n\t\t"views/{}.xml",'.format(view))
            file.write('\n\t\t"views/menu.xml"')
            file.write('\n\t],')
            file.write('\n\t"installable": True,')
            file.write('\n\t"application": True,')
            file.write('\n\t"license": "AGPL-3",')
            file.write('\n}')



module_name = input("Insert Module Name : ")
path_to_csv = input("Insert Path to CSV : ")
path_to_save = input("Insert Path to Save : ")
ModuleBuilder(module_name, path_to_csv, path_to_save)
