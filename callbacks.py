from dash.dependencies import Input, Output, State, MATCH
from app import dash_app
from dash.exceptions import PreventUpdate
import dash
import os
import json
import pandas as pd
import base64
import MAIN_TAB
import refBalance
import Reg2_Orders

import layouts
import dash_audio_components
#
# import Orders
# import datetime as dt
#
# from decimal import ROUND_UP,Context



dash_app.config['suppress_callback_exceptions'] = True
# dash_app.config['serve_locally'] = True
main_path_data = os.path.abspath("./data")
dash_app.scripts.config.serve_locally = True
# Encode the local sound file.
sound_filename = (main_path_data + "\\signal.mp3")  # replace with your own .mp3 file
encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())



def refresh(app: dash.Dash):
    ###############################    RESTART ALL FUNCTIONS     ########################################
    @app.callback([Output('table', 'data'),
                   Output('valuta', 'data'),
                   Output('table_all', 'data'),
                   Output('placeholder1', 'children'),
                   ],
                  [
                      Input('interval', 'n_intervals'),
                  ],
                  [State('newval1_btn', "value"),
                   State('newval2_btn', "value"),
                   State('newval3_btn', "value"),
                   State('newbirga1_btn', "value"),
                   State('newbirga2_btn', "value"),
                   State('newbirga1_com_btn', "value"),
                   State('newbirga2_com_btn', "value"),
                   State('newprofit_btn', "value"),
                   State('neworder_com_btn', "value"),
                   State('newper_btn', "value"),
                   ]
                  )
    def trigger_by_modify(n_clicks, val1, val2, val3, birga1, birga2,birga1_com, birga2_com, profit, order, percent):

        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')
        # print('button_id :', button_id[0])
        # # print('n :', n)
        # print('n_clicks :',  n_clicks)

        valuta = pd.read_csv(main_path_data + "\\balance.csv")
        try:
            vilki = pd.read_csv(main_path_data + "\\vilki.csv")
        except Exception as e:
            vilki = pd.read_csv(main_path_data + "\\vilki.csv")
            pass
        final2 = pd.read_csv(main_path_data + "\\all_data.csv")

        # print(vilki)



        vilki['profit'] = vilki['profit'].map('{:,.2f}%'.format)
        vilki['kurs1'] = vilki['kurs1'].map('{:,.8f}'.format)
        vilki['kurs2'] = vilki['kurs2'].map('{:,.8f}'.format)
        vilki['Vol1'] = vilki['Vol1'].map('{:,.6f}'.format)
        vilki['Vol2'] = vilki['Vol2'].map('{:,.6f}'.format)
        vilki['Vol3'] = vilki['Vol3'].map('{:,.6f}'.format)
        vilki['Vol4'] = vilki['Vol4'].map('{:,.6f}'.format)

        valuta['alfa'] = valuta['alfa'].map('{:,.6f}'.format)
        valuta['live'] = valuta['live'].map('{:,.6f}'.format)
        valuta['hot'] = valuta['hot'].map('{:,.6f}'.format)
        valuta['Summa'] = valuta['Summa'].map('{:,.6f}'.format)

        final2['profit'] = final2['profit'].map('{:,.6f}'.format)
        final2['start'] = final2['start'].map('{:,.6f}'.format)
        final2['step'] = final2['step'].map('{:,.6f}'.format)
        final2['back'] = final2['back'].map('{:,.6f}'.format)
        final2['rates_x'] = final2['rates_x'].map('{:,.8f}'.format)
        final2['rates_y'] = final2['rates_y'].map('{:,.8f}'.format)
        final2['perc'] = final2['perc'].map('{:,.2f}%'.format)


        if button_id[0] == 'interval':
            print(" ##########   REFRESH  ################")
            if float(vilki.iloc[0]['kurs1']) > 0:
                print(" ##########   1  ################")
                return vilki.to_dict('records'),valuta.to_dict('records'),final2.to_dict('records'), layouts.sound(0)
            else:
                print(" ##########   2  ################")
                return vilki.to_dict('records'), valuta.to_dict('records'), final2.to_dict('records'), layouts.sound(1)

        else:
            raise PreventUpdate
def refresh2(app: dash.Dash):
    ###############################    RESTART ALL FUNCTIONS     ########################################
    @app.callback([Output('vilki2_table', 'data'),
                   Output('vilki2_all_table', 'data'),
                   ],
                  [
                      Input('interval2', 'n_intervals'),
                  ],
                  [State('newval1_btn_reg2', "value"),
                   State('newval2_btn_reg2', "value"),
                   State('newval3_btn_reg2', "value"),
                   State('newbirga1_btn_reg2', "value"),
                   State('newbirga2_btn_reg2', "value"),
                   State('newbirga1_com_btn_reg2', "value"),
                   State('newbirga2_com_btn_reg2', "value"),
                   State('newprofit_btn_reg2', "value"),
                   State('neworder_com_btn_reg2', "value"),
                   State('newper_btn_reg2', "value"),
                   ]
                  )
    def trigger_by_modify(n_clicks, val1, val2, val3, birga1, birga2,birga1_com, birga2_com, profit, order, percent):

        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')
        # print('button_id :', button_id[0])
        # # print('n :', n)
        # print('n_clicks :',  n_clicks)


        try:
            vilki = pd.read_csv(main_path_data + "\\vilki2.csv")
        except Exception as e:
            vilki = pd.read_csv(main_path_data + "\\vilki2.csv")
            pass
        final2 = pd.read_csv(main_path_data + "\\vilki2_all.csv")

        # print(vilki)



        vilki['profit'] = vilki['profit'].map('{:,.2f}%'.format)
        vilki['rates_x'] = vilki['rates_x'].map('{:,.8f}'.format)
        vilki['rates_y'] = vilki['rates_y'].map('{:,.8f}'.format)
        vilki['Vol1'] = vilki['Vol1'].map('{:,.6f}'.format)
        vilki['Vol2'] = vilki['Vol2'].map('{:,.6f}'.format)
        vilki['Vol3'] = vilki['Vol3'].map('{:,.6f}'.format)
        vilki['Vol4'] = vilki['Vol4'].map('{:,.6f}'.format)

        vilki['My_kurs'] = vilki['My_kurs'].map('{:,.6f}'.format)
        vilki['min_kurs'] = vilki['min_kurs'].map('{:,.6f}'.format)
        vilki['percent'] = vilki['percent'].map('{:,.2f}'.format)
        vilki['0_kurs'] = vilki['0_kurs'].map('{:,.6f}'.format)




        final2['profit'] = final2['profit'].map('{:,.6f}'.format)
        # final2['prof'] = final2['prof'].map('{:,.6f}'.format)
        # final2['per'] = final2['per'].map('{:,.2f}'.format)

        vilki['My_kurs'] = vilki['My_kurs'].map('{:,.6f}'.format)
        vilki['min_kurs'] = vilki['min_kurs'].map('{:,.6f}'.format)
        vilki['Bal1'] = vilki['Bal1'].map('{:,.6f}'.format)
        vilki['Bal2'] = vilki['Bal2'].map('{:,.6f}'.format)

        final2['kurs1'] = final2['kurs1'].map('{:,.8f}'.format)
        final2['kurs2'] = final2['kurs2'].map('{:,.8f}'.format)
        # final2['percent'] = final2['percent'].map('{:,.2f}%'.format)


        if button_id[0] == 'interval2':
            print(" ##########   REFRESH  ################")

            return vilki.to_dict('records'),final2.to_dict('records')


        else:
            raise PreventUpdate
def refresh3(app: dash.Dash):
            ###############################    RESTART ALL FUNCTIONS     ########################################
            @app.callback([Output('vilki3_table', 'data'),
                           Output('vilki3_all_table', 'data'),
                           ],
                          [
                              Input('interval3', 'n_intervals'),
                          ],
                          [State('newval1_btn_reg3', "value"),
                           State('newval2_btn_reg3', "value"),
                           State('newval3_btn_reg3', "value"),
                           State('newbirga1_btn_reg3', "value"),
                           State('newbirga2_btn_reg3', "value"),
                           State('newbirga1_com_btn_reg3', "value"),
                           State('newbirga2_com_btn_reg3', "value"),
                           State('newprofit_btn_reg3', "value"),
                           State('neworder_com_btn_reg3', "value"),
                           State('newper_btn_reg3', "value"),
                           ]
                          )
            def trigger_by_modify(n_clicks, val1, val2, val3, birga1, birga2, birga1_com, birga2_com, profit, order,
                                  percent):

                ctx = dash.callback_context
                button_id = ctx.triggered[0]['prop_id'].split('.')
                # print('button_id :', button_id[0])
                # # print('n :', n)
                # print('n_clicks :',  n_clicks)

                try:
                    vilki = pd.read_csv(main_path_data + "\\vilki3.csv")
                except Exception as e:
                    vilki = pd.read_csv(main_path_data + "\\vilki3.csv")
                    pass
                final2 = pd.read_csv(main_path_data + "\\vilki2_all.csv")

                # print(vilki)

                vilki['profit'] = vilki['profit'].map('{:,.2f}%'.format)
                vilki['rates_x'] = vilki['rates_x'].map('{:,.8f}'.format)
                vilki['rates_y'] = vilki['rates_y'].map('{:,.8f}'.format)
                vilki['Vol1'] = vilki['Vol1'].map('{:,.6f}'.format)
                vilki['Vol2'] = vilki['Vol2'].map('{:,.6f}'.format)
                vilki['Vol3'] = vilki['Vol3'].map('{:,.6f}'.format)
                vilki['Vol4'] = vilki['Vol4'].map('{:,.6f}'.format)

                vilki['My_kurs'] = vilki['My_kurs'].map('{:,.6f}'.format)
                vilki['min_kurs'] = vilki['min_kurs'].map('{:,.6f}'.format)
                vilki['percent'] = vilki['percent'].map('{:,.2f}'.format)
                vilki['0_kurs'] = vilki['0_kurs'].map('{:,.6f}'.format)

                # final2['profit'] = final2['profit'].map('{:,.6f}'.format)
                # final2['prof'] = final2['prof'].map('{:,.6f}'.format)
                # final2['per'] = final2['per'].map('{:,.2f}'.format)

                vilki['My_kurs'] = vilki['My_kurs'].map('{:,.6f}'.format)
                vilki['min_kurs'] = vilki['min_kurs'].map('{:,.6f}'.format)
                vilki['Bal1'] = vilki['Bal1'].map('{:,.6f}'.format)
                vilki['Bal2'] = vilki['Bal2'].map('{:,.6f}'.format)

                # final2['rates_x'] = final2['rates_x'].map('{:,.8f}'.format)
                # final2['rates_y'] = final2['rates_y'].map('{:,.8f}'.format)
                # final2['percent'] = final2['percent'].map('{:,.2f}%'.format)

                if button_id[0] == 'interval3':
                    print(" ##########   REFRESH  ################")
                    return vilki.to_dict('records'), final2.to_dict('records')
                else:
                    raise PreventUpdate

def save_key_data(app: dash.Dash):
    @app.callback(

        [Output({'type': 'key', 'index': MATCH}, 'placeholder'),
         Output({'type': 'api', 'index': MATCH}, 'placeholder')],
        [Input({'type': 'save_btn', 'index': MATCH}, 'n_clicks')],
        [State({'type': 'save_btn', 'index': MATCH}, 'id'),
         State({'type': 'key', 'index': MATCH}, 'value'),
         State({'type': 'api', 'index': MATCH}, 'value'),
         ])
    def display_output(n_clicks, id, key, api):
        if n_clicks is None:
            raise PreventUpdate

        else:


            a_file = open(main_path_data + "\\keys.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            json_object[str(id['index'])]['key'] = key
            json_object[str(id['index'])]['api'] = api
            print("###################################  keys JSON NEW:", '\n', json_object)
            a_file = open(main_path_data + "\\keys.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            return "{}".format(key), "{}".format(api)

def creat_reg(app: dash.Dash):

    @app.callback([Output('listcardreg', 'children')],
        [Input('Create_NewRegim_btn', 'n_clicks'),
         Input('On_Avtomat_btn', 'n_clicks'),
         Input('Off_Avtomat_btn', 'n_clicks')],
                  [State('newval1_btn', "value"),
                   State('newval2_btn', "value"),
                   State('newval3_btn', "value"),
                   State('newbirga1_btn', "value"),
                   State('newbirga2_btn', "value"),
                   State('newbirga1_com_btn', "value"),
                   State('newbirga2_com_btn', "value"),
                   State('newprofit_btn', "value"),
                   State('neworder_com_btn', "value"),
                   State('newper_btn', "value"),
                   ])

    def create(n_clicks, n_clicks2,n_clicks3, val1, val2, val3, birga1, birga2,birga1_com, birga2_com, profit, order, percent):

        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')
        print('button_id  1:', button_id[0])
        print('n_clicks 1 :',  n_clicks)

        if button_id[0] == 'Create_NewRegim_btn':
            if n_clicks > 0:
                print('\n', '\n',"##########################  NEW REGIM:", '\n', '\n')
                # with open(main_path_data + "\\new_regims.json", "r") as file:
                file = open(main_path_data + "\\new_regims.json", "r")
                param = []
                data = json.load(file)
                file.close()
                for k, v in data.items():
                    param.append(k)

                if not param:
                    next_id = 1
                    data[next_id] = {"birga1": birga1,
                     "birga2": birga2,
                     "val1": val1,
                     "val2": val2,
                     "val3": val3,
                     "birga1_com": birga1_com,
                     "birga2_com": birga2_com,
                     "profit": profit,
                     "order": order,
                     "per": percent,
                     "avtomat": "off"
                     }
                    f = open(main_path_data + "\\new_regims.json", "w")
                    json.dump(data, f)
                    f.close()
                    list_group = [i for i in MAIN_TAB.regims()]
                    return [list_group]
                else:
                    next_id = str(int(param[-1]) + 1)
                    data[next_id] = {"birga1": birga1,
                     "birga2": birga2,
                     "val1": val1,
                     "val2": val2,
                     "val3": val3,
                     "birga1_com": birga1_com,
                     "birga2_com": birga2_com,
                     "profit": profit,
                     "order": order,
                     "per": percent,
                     "avtomat": "off"
                     }
                    f = open(main_path_data + "\\new_regims.json", "w")
                    json.dump(data, f)
                    f.close()
                    list_group = [i for i in MAIN_TAB.regims()]
                    return [list_group]
            else:
                raise PreventUpdate
        elif button_id[0] == 'On_Avtomat_btn':
            print("AVTOMAT ON")
            # with open(main_path_data + "\\new_regims.json", "r") as file:
            file = open(main_path_data + "\\new_regims.json", "r")
            data = json.load(file)
            file.close()
            for k, v in data.items():
                v['avtomat'] = 'on'

            f = open(main_path_data + "\\new_regims.json", "w")
            json.dump(data, f)
            f.close()
            list_group = [i for i in MAIN_TAB.regims()]
            return [list_group]
        elif button_id[0] == 'Off_Avtomat_btn':
            print("AVTOMAT OFF")
            # with open(main_path_data + "\\new_regims.json", "r") as file:
            file = open(main_path_data + "\\new_regims.json", "r")
            data = json.load(file)
            file.close()
            for k, v in data.items():
                v['avtomat'] = 'off'

            f = open(main_path_data + "\\new_regims.json", "w")
            json.dump(data, f)
            f.close()
            list_group = [i for i in MAIN_TAB.regims()]
            return [list_group]
        else:
            raise PreventUpdate
def creat_reg2(app: dash.Dash):

    @app.callback([Output('listcardreg2', 'children')],
        [Input('Create_NewRegim_btn_reg2', 'n_clicks'),
         Input('On_Avtomat_btn_reg2', 'n_clicks'),
         Input('Off_Avtomat_btn_reg2', 'n_clicks')],
                  [State('newval1_btn_reg2', "value"),
                   State('newval2_btn_reg2', "value"),
                   State('newval3_btn_reg2', "value"),
                   State('newbirga1_btn_reg2', "value"),
                   State('newbirga2_btn_reg2', "value"),
                   State('newbirga1_com_btn_reg2', "value"),
                   State('newbirga2_com_btn_reg2', "value"),
                   State('newprofit_btn_reg2', "value"),
                   State('neworder_com_btn_reg2', "value"),
                   State('newper_btn_reg2', "value"),
                   ])

    def create(n_clicks, n_clicks2,n_clicks3, val1, val2, val3, birga1, birga2,birga1_com, birga2_com, profit, order, percent):

        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')

        if button_id[0] == 'Create_NewRegim_btn_reg2':
            if n_clicks > 0:
                print('\n', '\n',"##########################  NEW REGIM:", '\n', '\n')
                # with open(main_path_data + "\\new_regims.json", "r") as file:
                file = open(main_path_data + "\\regims2.json", "r")
                param = []
                data = json.load(file)
                file.close()
                for k, v in data.items():
                    param.append(k)

                if not param:
                    next_id = 1
                    data[next_id] = {"birga1": birga1,
                     "birga2": birga2,
                     "val1": val1,
                     "val2": val2,
                     "val3": val3,
                     "birga1_com": birga1_com,
                     "birga2_com": birga2_com,
                     "profit": profit,
                     "order": order,
                     "per": percent,
                     "avtomat": "off"
                     }
                    f = open(main_path_data + "\\regims2.json", "w")
                    json.dump(data, f)
                    f.close()
                    list_group = [i for i in MAIN_TAB.regims2()]
                    return [list_group]
                else:
                    next_id = str(int(param[-1]) + 1)
                    data[next_id] = {"birga1": birga1,
                     "birga2": birga2,
                     "val1": val1,
                     "val2": val2,
                     "val3": val3,
                     "birga1_com": birga1_com,
                     "birga2_com": birga2_com,
                     "profit": profit,
                     "order": order,
                     "per": percent,
                     "avtomat": "off"
                     }
                    f = open(main_path_data + "\\regims2.json", "w")
                    json.dump(data, f)
                    f.close()
                    list_group = [i for i in MAIN_TAB.regims2()]
                    return [list_group]
            else:
                raise PreventUpdate
        elif button_id[0] == 'On_Avtomat_btn_reg2':
            print("AVTOMAT ON")
            # with open(main_path_data + "\\new_regims.json", "r") as file:
            file = open(main_path_data + "\\regims2.json", "r")
            data = json.load(file)
            file.close()
            for k, v in data.items():
                v['avtomat'] = 'on'

            f = open(main_path_data + "\\regims2.json", "w")
            json.dump(data, f)
            f.close()
            list_group = [i for i in MAIN_TAB.regims2()]
            return [list_group]
        elif button_id[0] == 'Off_Avtomat_btn_reg2':
            print("AVTOMAT OFF")
            # with open(main_path_data + "\\new_regims.json", "r") as file:
            file = open(main_path_data + "\\regims2.json", "r")
            data = json.load(file)
            file.close()
            for k, v in data.items():
                v['avtomat'] = 'off'

            f = open(main_path_data + "\\regims2.json", "w")
            json.dump(data, f)
            f.close()
            list_group = [i for i in MAIN_TAB.regims2()]
            return [list_group]
        else:
            raise PreventUpdate
def creat_reg3(app: dash.Dash):

    @app.callback([Output('listcardreg3', 'children')],
        [Input('Create_NewRegim_btn_reg3', 'n_clicks'),
         Input('On_Avtomat_btn_reg3', 'n_clicks'),
         Input('Off_Avtomat_btn_reg3', 'n_clicks')],
                  [State('newval1_btn_reg3', "value"),
                   State('newval2_btn_reg3', "value"),
                   State('newval3_btn_reg3', "value"),
                   State('newbirga1_btn_reg3', "value"),
                   State('newbirga2_btn_reg3', "value"),
                   State('newbirga1_com_btn_reg3', "value"),
                   State('newbirga2_com_btn_reg3', "value"),
                   State('newprofit_btn_reg3', "value"),
                   State('neworder_com_btn_reg3', "value"),
                   State('newper_btn_reg3', "value"),
                   ])

    def create(n_clicks, n_clicks2,n_clicks3, val1, val2, val3, birga1, birga2,birga1_com, birga2_com, profit, order, percent):

        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')

        if button_id[0] == 'Create_NewRegim_btn_reg3':
            if n_clicks > 0:
                print('\n', '\n',"##########################  NEW REGIM:", '\n', '\n')
                # with open(main_path_data + "\\new_regims.json", "r") as file:
                file = open(main_path_data + "\\regims3.json", "r")
                param = []
                data = json.load(file)
                file.close()
                for k, v in data.items():
                    param.append(k)

                if not param:
                    next_id = 1
                    data[next_id] = {"birga1": birga1,
                     "birga2": birga2,
                     "val1": val1,
                     "val2": val2,
                     "val3": val3,
                     "birga1_com": birga1_com,
                     "birga2_com": birga2_com,
                     "profit": profit,
                     "order": order,
                     "per": percent,
                     "avtomat": "off"
                     }
                    f = open(main_path_data + "\\regims2.json", "w")
                    json.dump(data, f)
                    f.close()
                    list_group = [i for i in MAIN_TAB.regims3()]
                    return [list_group]
                else:
                    next_id = str(int(param[-1]) + 1)
                    data[next_id] = {"birga1": birga1,
                     "birga2": birga2,
                     "val1": val1,
                     "val2": val2,
                     "val3": val3,
                     "birga1_com": birga1_com,
                     "birga2_com": birga2_com,
                     "profit": profit,
                     "order": order,
                     "per": percent,
                     "avtomat": "off"
                     }
                    f = open(main_path_data + "\\regims3.json", "w")
                    json.dump(data, f)
                    f.close()
                    list_group = [i for i in MAIN_TAB.regims3()]
                    return [list_group]
            else:
                raise PreventUpdate
        elif button_id[0] == 'On_Avtomat_btn_reg3':
            print("AVTOMAT ON")
            # with open(main_path_data + "\\new_regims.json", "r") as file:
            file = open(main_path_data + "\\regims3.json", "r")
            data = json.load(file)
            file.close()
            for k, v in data.items():
                v['avtomat'] = 'on'

            f = open(main_path_data + "\\regims3.json", "w")
            json.dump(data, f)
            f.close()
            list_group = [i for i in MAIN_TAB.regims3()]
            return [list_group]
        elif button_id[0] == 'Off_Avtomat_btn_reg3':
            print("AVTOMAT OFF")
            # with open(main_path_data + "\\new_regims.json", "r") as file:
            file = open(main_path_data + "\\regims3.json", "r")
            data = json.load(file)
            file.close()
            for k, v in data.items():
                v['avtomat'] = 'off'

            f = open(main_path_data + "\\regims3.json", "w")
            json.dump(data, f)
            f.close()
            list_group = [i for i in MAIN_TAB.regims3()]
            return [list_group]
        else:
            raise PreventUpdate

def save_newreg_data(app: dash.Dash):
    @app.callback(
        [Output({'type': 'hidden_newreg', 'index': MATCH}, 'children'),
         Output({'type': 'Turn_Avtomat_btn', 'index': MATCH}, 'style'),
         Output({'type': 'Turn_Avtomat_btn', 'index': MATCH}, 'children')],
        [Input({'type': 'Save_NewRegim_btn', 'index': MATCH}, 'n_clicks'),
         Input({'type': 'Turn_Avtomat_btn', 'index': MATCH}, 'n_clicks'),
         Input({'type': 'Delete_NewRegim_btn', 'index': MATCH}, 'n_clicks')],
        [State({'type': 'Save_NewRegim_btn', 'index': MATCH}, 'id'),
         State({'type': 'newval1', 'index': MATCH}, "value"),
         State({'type': 'newval2', 'index': MATCH}, "value"),
         State({'type': 'newval3', 'index': MATCH}, "value"),
         State({'type': 'newbirga1', 'index': MATCH}, "value"),
         State({'type': 'newbirga2', 'index': MATCH}, "value"),
         # State({'type': 'newbirga1_com', 'index': MATCH}, "value"),
         # State({'type': 'newbirga2_com', 'index': MATCH}, "value"),
         State({'type': 'newprofit', 'index': MATCH}, "value"),
         State({'type': 'neworder_com', 'index': MATCH}, "value"),
         State({'type': 'newper', 'index': MATCH}, "value"),
         ]
    )


    def save_output(n_clicks, n_clicks2, n_clicks3, id, val1, val2, val3, birga1, birga2,profit, order, percent):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')

        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate
        elif n_clicks> 0 or n_clicks2> 0 or n_clicks3> 0:
            pass
        else:
            raise dash.exceptions.PreventUpdate


        # print('button_id 2 :', button_id[0])

        bb = button_id[0]
        d = json.loads(bb)


        if order is None:
            order = ""
        else:
            order = order

        if percent is None:
            percent = ""
        else:
            percent = percent



        if d['type'] == 'Save_NewRegim_btn':
            print("#########     SAVED    ##############")
            a_file = open(main_path_data + "\\new_regims.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            json_object[d['index']]['val1'] = val1
            json_object[d['index']]['val2'] = val2
            json_object[d['index']]['val3'] = val3
            json_object[d['index']]['birga1'] = birga1
            json_object[d['index']]['birga2'] = birga2
            # json_object[d['index']]['birga1_com'] = birga1_com
            # json_object[d['index']]['birga2_com'] = birga2_com
            json_object[d['index']]['profit'] = float(profit)
            json_object[d['index']]['order'] = order
            json_object[d['index']]['per'] = percent

            if json_object[d['index']]['avtomat'] == 'on':
                style = {'text-align': 'center',
                         "background-color": "palegreen",
                               'max-width': '50px','padding': '0',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'on'
            else:
                style = {'text-align': 'center',
                         "background-color": "tomato",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'off'

            a_file = open(main_path_data + "\\new_regims.json", "w")
            json.dump(json_object, a_file)
            a_file.close()

            return [""], style, butt
        elif d['type'] == 'Turn_Avtomat_btn':
            print("#########     AVTOMAT    ##############")
            a_file = open(main_path_data + "\\new_regims.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            if json_object[d['index']]['avtomat'] == 'on':
                json_object[d['index']]['avtomat'] = 'off'
                style = {'text-align': 'center',
                         "background-color": "tomato",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'off'
            else:
                json_object[d['index']]['avtomat'] = 'on'
                style = {'text-align': 'center',
                         "background-color": "palegreen",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'on'


            a_file = open(main_path_data + "\\new_regims.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            return [""], style, butt
        elif d['type'] == 'Delete_NewRegim_btn':
            print("#########     DELETED    ##############")
            a_file = open(main_path_data + "\\new_regims.json", "r")
            json_object = json.load(a_file)
            a_file.close()

            del json_object[d['index']]
            style = {'text-align': 'center',
                     "background-color": "tomato",
                     "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
            butt = 'DELETED'
            a_file = open(main_path_data + "\\new_regims.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            return [""], style, butt
        else:
            raise dash.exceptions.PreventUpdate
def save_newreg2_data(app: dash.Dash):
    @app.callback(
        [Output({'type': 'hidden_newreg_reg2', 'index': MATCH}, 'children'),
         Output({'type': 'Turn_Avtomat_btn_reg2', 'index': MATCH}, 'style'),
         Output({'type': 'Turn_Avtomat_btn_reg2', 'index': MATCH}, 'children')],
        [Input({'type': 'Save_NewRegim_btn_reg2', 'index': MATCH}, 'n_clicks'),
         Input({'type': 'Turn_Avtomat_btn_reg2', 'index': MATCH}, 'n_clicks'),
         Input({'type': 'Delete_NewRegim_btn_reg2', 'index': MATCH}, 'n_clicks')],
        [State({'type': 'Save_NewRegim_btn_reg2', 'index': MATCH}, 'id'),
         State({'type': 'newval1_reg2', 'index': MATCH}, "value"),
         State({'type': 'newval2_reg2', 'index': MATCH}, "value"),
         State({'type': 'newval3_reg2', 'index': MATCH}, "value"),
         State({'type': 'newbirga1_reg2', 'index': MATCH}, "value"),
         State({'type': 'newbirga2_reg2', 'index': MATCH}, "value"),
         State({'type': 'newprofit_reg2', 'index': MATCH}, "value"),
         State({'type': 'neworder_com_reg2', 'index': MATCH}, "value"),
         State({'type': 'newper_reg2', 'index': MATCH}, "value"),
         ]
    )


    def save_output(n_clicks, n_clicks2, n_clicks3, id, val1, val2, val3, birga1, birga2,profit, order, percent):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')

        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate
        elif n_clicks> 0 or n_clicks2> 0 or n_clicks3> 0:
            pass
        else:
            raise dash.exceptions.PreventUpdate


        bb = button_id[0]
        d = json.loads(bb)


        if order is None:
            order = ""
        else:
            order = order

        if percent is None:
            percent = ""
        else:
            percent = percent



        if d['type'] == 'Save_NewRegim_btn_reg2':
            print("#########     SAVED    ##############")
            a_file = open(main_path_data + "\\regims2.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            json_object[d['index']]['val1'] = val1
            json_object[d['index']]['val2'] = val2
            json_object[d['index']]['val3'] = val3
            json_object[d['index']]['birga1'] = birga1
            json_object[d['index']]['birga2'] = birga2
            json_object[d['index']]['profit'] = float(profit)
            json_object[d['index']]['order'] = order
            json_object[d['index']]['per'] = percent

            if json_object[d['index']]['avtomat'] == 'on':
                style = {'text-align': 'center',
                         "background-color": "palegreen",
                               'max-width': '50px','padding': '0',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'on'
            else:
                style = {'text-align': 'center',
                         "background-color": "tomato",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'off'

            a_file = open(main_path_data + "\\regims2.json", "w")
            json.dump(json_object, a_file)
            a_file.close()

            return [""], style, butt
        elif d['type'] == 'Turn_Avtomat_btn_reg2':
            print("#########     AVTOMAT  2  ##############")
            a_file = open(main_path_data + "\\regims2.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            if json_object[d['index']]['avtomat'] == 'on':
                json_object[d['index']]['avtomat'] = 'off'
                style = {'text-align': 'center',
                         "background-color": "tomato",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'off'
                vilki2 = pd.read_csv(main_path_data + "\\vilki2.csv")

                vv = vilki2[vilki2["regim"] == int(d['index'])]
                if vv.shape[0]>0:
                    bir = vv.iloc[0]['birga_x']
                    if bir == 'alfa':
                        reponse2 = Reg2_Orders.alfa_cancel(vv.iloc[0]['order_id'])
                    elif bir == 'live':
                        reponse2 = Reg2_Orders.live_cancel(vv.iloc[0]['valin_x'],vv.iloc[0]['valout_x'],vv.iloc[0]['order_id'])
                    elif bir == 'hot':
                        reponse2 = Reg2_Orders.hot_cancel(vv.iloc[0]['valin_x'],vv.iloc[0]['valout_x'],vv.iloc[0]['order_id'])
                    else:
                        reponse2 = "No such BIRGA"
                        pass
                    vilki2.drop(vilki2.index[int(d['index'])], inplace=True)
                    vilki2.to_csv(main_path_data + "\\vilki2.csv", header=True, index=False)

            else:
                json_object[d['index']]['avtomat'] = 'on'
                style = {'text-align': 'center',
                         "background-color": "palegreen",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'on'


            a_file = open(main_path_data + "\\regims2.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            return [""], style, butt
        elif d['type'] == 'Delete_NewRegim_btn_reg2':
            print("#########     DELETED    ##############")
            a_file = open(main_path_data + "\\regims2.json", "r")
            json_object = json.load(a_file)
            a_file.close()

            del json_object[d['index']]
            style = {'text-align': 'center',
                     "background-color": "tomato",
                     "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
            butt = 'DELETED'
            a_file = open(main_path_data + "\\regims2.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            return [""], style, butt
        else:
            raise dash.exceptions.PreventUpdate
def save_newreg3_data(app: dash.Dash):
    @app.callback(
        [Output({'type': 'hidden_newreg_reg3', 'index': MATCH}, 'children'),
         Output({'type': 'Turn_Avtomat_btn_reg3', 'index': MATCH}, 'style'),
         Output({'type': 'Turn_Avtomat_btn_reg3', 'index': MATCH}, 'children')],
        [Input({'type': 'Save_NewRegim_btn_reg3', 'index': MATCH}, 'n_clicks'),
         Input({'type': 'Turn_Avtomat_btn_reg3', 'index': MATCH}, 'n_clicks'),
         Input({'type': 'Delete_NewRegim_btn_reg3', 'index': MATCH}, 'n_clicks')],
        [State({'type': 'Save_NewRegim_btn_reg3', 'index': MATCH}, 'id'),
         State({'type': 'newval1_reg3', 'index': MATCH}, "value"),
         State({'type': 'newval2_reg3', 'index': MATCH}, "value"),
         State({'type': 'newval3_reg3', 'index': MATCH}, "value"),
         State({'type': 'newbirga1_reg3', 'index': MATCH}, "value"),
         State({'type': 'newbirga2_reg3', 'index': MATCH}, "value"),
         State({'type': 'newprofit_reg3', 'index': MATCH}, "value"),
         State({'type': 'neworder_com_reg3', 'index': MATCH}, "value"),
         State({'type': 'newper_reg3', 'index': MATCH}, "value"),
         ]
    )


    def save_output(n_clicks, n_clicks2, n_clicks3, id, val1, val2, val3, birga1, birga2,profit, order, percent):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')

        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate
        elif n_clicks> 0 or n_clicks2> 0 or n_clicks3> 0:
            pass
        else:
            raise dash.exceptions.PreventUpdate


        bb = button_id[0]
        d = json.loads(bb)


        if order is None:
            order = ""
        else:
            order = order

        if percent is None:
            percent = ""
        else:
            percent = percent



        if d['type'] == 'Save_NewRegim_btn_reg3':
            print("#########     SAVED    ##############")
            a_file = open(main_path_data + "\\regims3.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            json_object[d['index']]['val1'] = val1
            json_object[d['index']]['val2'] = val2
            json_object[d['index']]['val3'] = val3
            json_object[d['index']]['birga1'] = birga1
            json_object[d['index']]['birga2'] = birga2
            json_object[d['index']]['profit'] = float(profit)
            json_object[d['index']]['order'] = order
            json_object[d['index']]['per'] = percent

            if json_object[d['index']]['avtomat'] == 'on':
                style = {'text-align': 'center',
                         "background-color": "palegreen",
                               'max-width': '50px','padding': '0',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'on'
            else:
                style = {'text-align': 'center',
                         "background-color": "tomato",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'off'

            a_file = open(main_path_data + "\\regims3.json", "w")
            json.dump(json_object, a_file)
            a_file.close()

            return [""], style, butt
        elif d['type'] == 'Turn_Avtomat_btn_reg3':
            print("#########     AVTOMAT  2  ##############")
            a_file = open(main_path_data + "\\regims3.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            if json_object[d['index']]['avtomat'] == 'on':
                json_object[d['index']]['avtomat'] = 'off'
                style = {'text-align': 'center',
                         "background-color": "tomato",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'off'
                vilki2 = pd.read_csv(main_path_data + "\\vilki3.csv")

                vv = vilki2[vilki2["regim"] == int(d['index'])]
                if vv.shape[0]>0:
                    bir = vv.iloc[0]['birga_x']
                    if bir == 'alfa':
                        reponse2 = Reg2_Orders.alfa_cancel(vv.iloc[0]['order_id'])
                    elif bir == 'live':
                        reponse2 = Reg2_Orders.live_cancel(vv.iloc[0]['valin_x'],vv.iloc[0]['valout_x'],vv.iloc[0]['order_id'])
                    elif bir == 'hot':
                        reponse2 = Reg2_Orders.hot_cancel(vv.iloc[0]['valin_x'],vv.iloc[0]['valout_x'],vv.iloc[0]['order_id'])
                    else:
                        reponse2 = "No such BIRGA"
                        pass
                    vilki2.drop(vilki2.index[int(d['index'])], inplace=True)
                    vilki2.to_csv(main_path_data + "\\vilki3.csv", header=True, index=False)

            else:
                json_object[d['index']]['avtomat'] = 'on'
                style = {'text-align': 'center',
                         "background-color": "palegreen",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'on'


            a_file = open(main_path_data + "\\regims3.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            return [""], style, butt
        elif d['type'] == 'Delete_NewRegim_btn_reg3':
            print("#########     DELETED    ##############")
            a_file = open(main_path_data + "\\regims3.json", "r")
            json_object = json.load(a_file)
            a_file.close()

            del json_object[d['index']]
            style = {'text-align': 'center',
                     "background-color": "tomato",
                     "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
            butt = 'DELETED'
            a_file = open(main_path_data + "\\regims3.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            return [""], style, butt
        else:
            raise dash.exceptions.PreventUpdate

def ref_balance(app: dash.Dash):
    @app.callback(
        [Output('BALANCE-content', 'children')],
        [Input('Ref_balance_btn', 'n_clicks')])
    def display_output(n_clicks):

        if n_clicks is None:
            raise PreventUpdate
        elif n_clicks > 0:
            print("REFRESHED BALANCE")
            refBalance.NewBalance()
            return ["0"]
        else:
            raise PreventUpdate






refresh(dash_app)
refresh2(dash_app)
refresh3(dash_app)
save_key_data(dash_app)
creat_reg(dash_app)
creat_reg2(dash_app)
creat_reg3(dash_app)
save_newreg_data(dash_app)
save_newreg2_data(dash_app)
save_newreg3_data(dash_app)
ref_balance(dash_app)

