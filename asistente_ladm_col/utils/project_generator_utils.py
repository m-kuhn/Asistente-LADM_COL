# -*- coding: utf-8 -*-
"""
/***************************************************************************
                              Asistente LADM_COL
                             --------------------
        begin                : 2018-02-06
        git sha              : :%H$
        copyright            : (C) 2018 by Germán Carrillo (BSF Swissphoto)
        email                : gcarrillo@linuxmail.org
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License v3.0 as          *
 *   published by the Free Software Foundation.                            *
 *                                                                         *
 ***************************************************************************/
"""
import qgis
from qgis.PyQt.QtCore import QObject
from qgis.core import (QgsProject,
                       Qgis,
                       QgsApplication)

from .domains_parser import DomainRelationGenerator
from ..config.general_config import (PLUGIN_NAME,
                                     KIND_SETTINGS,
                                     TABLE_NAME,
                                     RELATION_NAME,
                                     REFERENCED_LAYER,
                                     REFERENCED_FIELD,
                                     REFERENCING_LAYER,
                                     REFERENCING_FIELD,
                                     RELATION_TYPE,
                                     CLASS_CLASS_RELATION,
                                     translated_strings)
from ..config.table_mapping_config import (TABLE_PROP_DOMAIN,
                                           TABLE_PROP_STRUCTURE)


class ProjectGeneratorUtils(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.log = QgsApplication.messageLog()

    def get_generator(self, db):
        if 'projectgenerator' in qgis.utils.plugins:
            projectgenerator = qgis.utils.plugins["projectgenerator"]
            generator = projectgenerator.get_generator()("ili2pg" if db.mode=="pg" else "ili2gpkg",
                db.uri, "smart2", db.schema, pg_estimated_metadata=False)
            return generator
        else:
            self.log.logMessage(
                "El plugin Project Generator es un prerrequisito, instálalo antes de usar Asistente LADM_COL.",
                PLUGIN_NAME,
                Qgis.Critical
            )
            return None

    def get_db_connection(self, db):
        generator = self.get_generator(db)
        if generator is not None:
            return generator._db_connector

        return None

    def load_layers(self, layer_list, db):
        """
        Load a selected list of layers from project generator.
        This call should configure relations and bag of enums
        between layers being loaded, but not when a layer already
        loaded has a relation or is part of a bag of enum. For
        that case, we use a cached set of relations and bags of
        enums that we get only once per session and configure in
        the Asistente LADM_COL.
        """
        if 'projectgenerator' in qgis.utils.plugins:
            projectgenerator = qgis.utils.plugins["projectgenerator"]
            generator = projectgenerator.get_generator()("ili2pg" if db.mode=="pg" else "ili2gpkg",
                db.uri, "smart2", db.schema, pg_estimated_metadata=False)
            layers = generator.layers(layer_list)
            relations, bags_of_enum = generator.relations(layers, layer_list)
            legend = generator.legend(layers, ignore_node_names=[translated_strings.ERROR_LAYER_GROUP])
            projectgenerator.create_project(layers, relations, bags_of_enum, legend, auto_transaction=False)
        else:
            self.log.logMessage(
                "El plugin Project Generator es un prerrequisito, instálalo antes de usar Asistente LADM_COL.",
                PLUGIN_NAME,
                Qgis.Critical
            )

    def get_layers_and_relations_info(self, db):
        """
        Called once per session, this is used to get information
        of all relations and bags of enums in the DB and cache it
        in the Asistente LADM_COL.
        """
        if 'projectgenerator' in qgis.utils.plugins:
            generator = self.get_generator(db)

            layers = generator.get_tables_info_without_ignored_tables()
            relations = generator.get_relations_info()
            relations = self.filter_relations(relations)

            domain_generator = DomainRelationGenerator(generator._db_connector, "smart2")
            layer_names = [record[TABLE_NAME] for record in layers]
            domain_names = [record[TABLE_NAME] for record in layers if record[KIND_SETTINGS] == TABLE_PROP_DOMAIN]
            structure_names = [record[TABLE_NAME] for record in layers if record[KIND_SETTINGS] == TABLE_PROP_STRUCTURE]
            domains, bags_of_enum = domain_generator.get_domain_relations_info(layer_names, domain_names, structure_names)

            return (layers, relations + domains, bags_of_enum)
        else:
            self.log.logMessage(
                "El plugin Project Generator es un prerrequisito, instálalo antes de usar Asistente LADM_COL.",
                PLUGIN_NAME,
                Qgis.Critical
            )
            return (None, None)

    def filter_relations(self, relations):
        filtered_relations = list()
        for relation in relations:
            if not relation[REFERENCING_FIELD].startswith('uej2_') and \
               not relation[REFERENCING_FIELD].startswith('ue_'):
                new_relation = {
                    RELATION_NAME: relation[RELATION_NAME],
                    REFERENCED_LAYER: relation[REFERENCED_LAYER],
                    REFERENCED_FIELD: relation[REFERENCED_FIELD],
                    REFERENCING_LAYER: relation[REFERENCING_LAYER],
                    REFERENCING_FIELD: relation[REFERENCING_FIELD],
                    RELATION_TYPE: CLASS_CLASS_RELATION
                }
                filtered_relations.append(new_relation)
        return filtered_relations

    def get_tables_info_without_ignored_tables(self, db):
        if 'projectgenerator' in qgis.utils.plugins:
            generator = self.get_generator(db)
            return generator.get_tables_info_without_ignored_tables()
        else:
            self.log.logMessage(
                "El plugin Project Generator es un prerrequisito, instálalo antes de usar Asistente LADM_COL.",
                PLUGIN_NAME,
                Qgis.Critical
            )

    def get_first_index_for_layer_type(self, layer_type, group=QgsProject.instance().layerTreeRoot()):
        if 'projectgenerator' in qgis.utils.plugins:
            import projectgenerator
            return projectgenerator.utils.qgis_utils.get_first_index_for_layer_type(layer_type, group)
        return None

    def get_suggested_index_for_layer(self, layer, group):
        if 'projectgenerator' in qgis.utils.plugins:
            import projectgenerator
            return projectgenerator.utils.qgis_utils.get_suggested_index_for_layer(layer, group)
        return None
