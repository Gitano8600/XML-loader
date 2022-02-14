import logging
import time
import typing

import pandas as pd
import xml.etree.ElementTree as ET

logger = logging.getLogger()


class OfacParser:
    def __init__(self):

        self._xmlns = '{http://tempuri.org/sdnList.xsd}'
        self._xml_data = None

        self.entry_columns = ['uid', 'lastName', 'firstName', 'sdnType', 'title', 'remarks']
        self.alias_columns = ['entry_uid', 'uid', 'type', 'category', 'lastName', 'firstName']
        self.program_columns = ['entry_uid', 'program']
        self.address_columns = ['entry_uid', 'uid', 'address1', 'address2', 'address3', 'city', 'stateOrProvince',
                                'postalCode', 'country']
        self.id_columns = ['entry_uid', 'uid', 'idType', 'idNumber', 'idCountry', 'issueDate', 'expirationDate']
        self.nationality_columns = ['entry_uid', 'uid', 'country', 'mainEntry']
        self.citizenship_columns = ['entry_uid', 'uid', 'country', 'mainEntry']
        self.dob_columns = ['entry_uid', 'uid', 'dateOfBirth', 'mainEntry']
        self.pob_columns = ['entry_uid', 'uid', 'placeOfBirth', 'mainEntry']
        self.vessel_info_columns = ['entry_uid', 'callSign', 'vesselType', 'vesselFlag', 'vesselOwner', 'tonnage',
                                    'grossRegisteredTonnage']

        self.df_entries = pd.DataFrame(columns=self.entry_columns)
        self.df_alias = pd.DataFrame(columns=self.alias_columns)
        self.df_program = pd.DataFrame(columns=self.program_columns)
        self.df_address = pd.DataFrame(columns=self.address_columns)
        self.df_id = pd.DataFrame(columns=self.id_columns)
        self.df_nationality = pd.DataFrame(columns=self.nationality_columns)
        self.df_citizenship = pd.DataFrame(columns=self.citizenship_columns)
        self.df_dob = pd.DataFrame(columns=self.dob_columns)
        self.df_pob = pd.DataFrame(columns=self.pob_columns)
        self.df_vessel_info = pd.DataFrame(columns=self.vessel_info_columns)

        self.logs = []



    def _add_log(self, msg: str):
        logger.info("%s", msg)
        self.logs.append({"log": msg, "displayed": False})

    def _parse_xml(self):
        logger.info("Binance connection opened")
        logger.info(self._xml_path)

    def get_text(self, tag: str, level):
        print(f'tag: {tag} / level: {level}')
        return level.find(f'{self._xmlns}{tag}').text if level.find(f'{self._xmlns}{tag}') is not None else ''

    def get_child(self, entry_uid, child, cols, df):
        row = []
        row.append(list(map(lambda p: self.get_text(p, child), cols[1:])))
        #print(row)
        row[0].insert(0, entry_uid)
        #print(row)
        row_to_append = pd.DataFrame(row, columns=cols)
        df = df.append(row_to_append, ignore_index=True)

        return df

    def parse_data(self, file_path: str):
        self._xml_data = ET.parse(file_path)

    def process_data(self):
        for node in self._xml_data.getroot():
            if node.tag == '{http://tempuri.org/sdnList.xsd}publshInformation':
                publish_date = ([publish_date.text for publish_date in node.findall(f'{self._xmlns}Publish_Date')][0])
                record_count = ([record_count.text for record_count in node.findall(f'{self._xmlns}Record_Count')][0])
                print(f'Loading SDN list of {publish_date} with {record_count} entries.')
            else:
                entry_uid = self.get_text('uid', node)
                entry_list = []
                entry_list.append(map(lambda p: self.get_text(p, node), self.entry_columns))

                row_to_append = pd.DataFrame(entry_list, columns=self.entry_columns)
                self.df_entries = self.df_entries.append(row_to_append, ignore_index=True)



                for akaList in node.findall(f'{self._xmlns}akaList'):
                    for child in akaList:
                        self.df_alias = self.get_child(entry_uid, child, self.alias_columns, self.df_alias)

                for programList in node.findall(f'{self._xmlns}programList'):
                    for child in programList:
                        self.df_program = self.get_child(entry_uid, child, self.program_columns, self.df_program)
                '''
                for addressList in node.findall(f'{self._xmlns}addressList'):
                    for child in addressList:
                        self.df_address = self.get_child(entry_uid, child, self.address_columns, self.df_address)

                for idList in node.findall(f'{self._xmlns}idList'):
                    for child in idList:
                        self.df_id = self.get_child(entry_uid, child, self.id_columns, self.df_id)

                for nationalityList in node.findall(f'{self._xmlns}nationalityList'):
                    for child in nationalityList:
                        self.df_nationality = self.get_child(entry_uid, child, self.nationality_columns, self.df_nationality)

                for citizenshipList in node.findall(f'{self._xmlns}citizenshipList'):
                    for child in citizenshipList:
                        self.df_citizenship = self.get_child(entry_uid, child, self.citizenship_columns, self.df_citizenship)

                for dobList in node.findall(f'{self._xmlns}dateOfBirthList'):
                    for child in dobList:
                        self.df_dob = self.get_child(entry_uid, child, self.dob_columns, self.df_dob)

                for pobList in node.findall(f'{self._xmlns}placeOfBirthList'):
                    for child in pobList:
                        self.df_pob = self.get_child(entry_uid, child, self.pob_columns, self.df_pob)
                '''

                for vesselinfo in node.findall(f'{self._xmlns}vesselInfo'):
                    for child in vesselinfo:
                        self.df_vessel_info = self.get_child(entry_uid, child, self.vessel_info_columns, self.df_vessel_info)

        print("doing the Excel")
        self.df_entries.to_csv("testfile.csv")
        self.df_alias.to_csv("testfile_alias.csv")
        self.df_program.to_csv("testfile_program.csv")
        # self.df_address.to_csv("testfile_address.csv")
        # self.df_id.to_csv("testfile_id.csv")
        # self.df_nationality.to_csv("testfile_nationality.csv")
        # self.df_citizenship.to_csv("testfile_citizenship.csv")
        # self.df_dob.to_csv("testfile_dob.csv")
        # self.df_pob.to_csv("testfile_pob.csv")
        self.df_vessel_info.to_csv("testfile_vessel_info.csv")


        print("GOTCHA")