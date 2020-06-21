import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import pandas as pd
import dash_table
import os
import json
import MAIN_TAB

import base64


main_path_data = os.path.abspath("./data")
pd.options.display.float_format = '${:.6f}'.format
# Encode the local sound file.
sound_filename = (main_path_data + "\\signal.mp3")  # replace with your own .mp3 file
encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())

########  MAIN PAGE MY  ##############

def tab_keys():


    a_file = open(main_path_data + "\\keys.json", "r")
    keys8 = json.load(a_file)
    a_file.close()
    tab_keys = [ddk.Card(style={'width': '50%', 'margin': '5px', 'background-color': '#e4e7e7a6'},
                         card_hover=True,
                         children=ddk.Block(width=100,
                                            style={'justify-content': 'center'},
                                            children=[
                                                ddk.Block(width=20,
                                                          children=html.H2('btc-Alpha',
                                                                           style={
                                                                               'text-align': 'center',
                                                                               'justify': 'center'})),
                                                ddk.Block(width=50,
                                                          children=[ddk.Block(width=100,
                                                                              children=dcc.Input(
                                                                                  placeholder=keys8["1"]['key'],
                                                                                  id={
                                                                                      'type': 'key',
                                                                                      'index': '1'
                                                                                  },
                                                                                  style={
                                                                                      'border': 'double',
                                                                                      'margin': '0',
                                                                                      'background-color': 'ivory',
                                                                                      'width': '-webkit-fill-available'})),
                                                                    ddk.Block(width=100,
                                                                              children=dcc.Input(
                                                                                  placeholder=keys8["1"]['api'],
                                                                                  id={
                                                                                      'type': 'api',
                                                                                      'index': '1'
                                                                                  },
                                                                                  style={
                                                                                      'border': 'double',
                                                                                      'margin': '0',
                                                                                      'background-color': 'ivory',
                                                                                      'width': '-webkit-fill-available'}))]),
                                                ddk.Block(width=30,
                                                          children=html.Button('Сохранить',
                                                                               id={
                                                                                   'type': 'save_btn',
                                                                                   'index': '1'
                                                                               },
                                                                               style={
                                                                                   'text-align': 'center',
                                                                                   'justify': 'center'})),
                                            ])),
                ddk.Card(style={'width': '50%', 'margin': '5px', 'background-color': '#e4e7e7a6'},
                         card_hover=True,
                         children=ddk.Block(width=100,
                                            style={'justify-content': 'center'},
                                            children=[ddk.Block(width=20,
                                                                children=html.H2('Livecoin',
                                                                                 style={
                                                                                   'text-align': 'center',
                                                                                   'justify': 'center'})),
                                                      ddk.Block(width=50,
                                                                children=[ddk.Block(width=100,
                                                                                    children=dcc.Input(
                                                                                        placeholder=keys8["2"]['key'],
                                                                                        id={
                                                                                            'type': 'key',
                                                                                            'index': '2'
                                                                                        },
                                                                                        style={
                                                                                            'border': 'double',
                                                                                            'margin': '0',
                                                                                            'background-color': 'ivory',
                                                                                            'width': '-webkit-fill-available'})),
                                                                          ddk.Block(width=100,
                                                                                    children=dcc.Input(
                                                                                        placeholder=keys8["2"]['api'],
                                                                                        id={
                                                                                            'type': 'api',
                                                                                            'index': '2'
                                                                                        },
                                                                                        style={
                                                                                            'border': 'double',
                                                                                            'margin': '0',
                                                                                            'background-color': 'ivory',
                                                                                            'width': '-webkit-fill-available'}))]),
                                                      ddk.Block(width=30,
                                                                children=html.Button('Сохранить',
                                                                                     id={
                                                                                         'type': 'save_btn',
                                                                                         'index': '2'
                                                                                     },
                                                                                     style={
                                                                                         'text-align': 'center',
                                                                                         'justify': 'center'})),
                                                      ])),
                ddk.Card(style={'width': '50%', 'margin': '5px', 'background-color': '#e4e7e7a6'},
                         card_hover=True,
                         children=ddk.Block(width=100,
                                            style={'justify-content': 'center'},
                                            children=[ddk.Block(width=20, children=html.H2('Hotbit',
                                                                                           style={
                                                                                               'text-align': 'center',
                                                                                               'justify': 'center'})),
                                                      ddk.Block(width=50,
                                                                children=[ddk.Block(width=100,
                                                                                    children=dcc.Input(
                                                                                        placeholder=keys8["3"]['key'],
                                                                                        id={
                                                                                            'type': 'key',
                                                                                            'index': '3'
                                                                                        },
                                                                                        style={
                                                                                            'border': 'double',
                                                                                            'margin': '0',
                                                                                            'background-color': 'ivory',
                                                                                            'width': '-webkit-fill-available'})),
                                                                          ddk.Block(width=100,
                                                                                    children=dcc.Input(
                                                                                        placeholder=keys8["3"]['api'],
                                                                                        id={
                                                                                            'type': 'api',
                                                                                            'index': '3'
                                                                                        },
                                                                                        style={
                                                                                            'border': 'double',
                                                                                            'margin': '0',
                                                                                            'background-color': 'ivory',
                                                                                            'width': '-webkit-fill-available'}))]),
                                                      ddk.Block(width=30,
                                                                children=html.Button('Сохранить',
                                                                                     id={
                                                                                         'type': 'save_btn',
                                                                                         'index': '3'
                                                                                     },
                                                                                     style={
                                                                                         'text-align': 'center',
                                                                                         'justify': 'center'})),
                                                      ])),
                ddk.Card(style={'width': '50%', 'margin': '5px', 'background-color': '#e4e7e7a6'},
                         card_hover=True, children=ddk.Block(width=100,
                                                             style={'justify-content': 'center'},
                                                             children=[ddk.Block(width=20,
                                                                                 children=html.H2(
                                                                                     'TELEGRAM')),
                                                                       ddk.Block(width=50, children=[
                                                                           ddk.Block(width=100,
                                                                                     children=dcc.Input(
                                                                                         placeholder=keys8["4"]['key'],
                                                                                         id={
                                                                                             'type': 'key',
                                                                                             'index': '4'
                                                                                         },
                                                                                         style={
                                                                                             'border': 'double',
                                                                                             'margin': '0',
                                                                                             'background-color': 'ivory',
                                                                                             'width': '-webkit-fill-available'})),
                                                                           ddk.Block(width=100,
                                                                                     children=dcc.Input(
                                                                                         placeholder=keys8["4"]['api'],
                                                                                         id={
                                                                                             'type': 'api',
                                                                                             'index': '4'
                                                                                         },
                                                                                         style={
                                                                                             'border': 'double',
                                                                                             'margin': '0',
                                                                                             'background-color': 'ivory',
                                                                                             'width': '-webkit-fill-available'}))]),
                                                                       ddk.Block(width=30,
                                                                                 children=html.Button(
                                                                                     'Сохранить',
                                                                                     id={
                                                                                         'type': 'save_btn',
                                                                                         'index': '4'
                                                                                     },
                                                                                     style={
                                                                                         'text-align': 'center',
                                                                                         'justify': 'center'})),
                                                                       ]))]

    return tab_keys

def serve_layout():
    interval = dcc.Interval(id='interval', interval=1000, n_intervals=0)
    valuta = pd.read_csv(main_path_data + "\\balance.csv")
    vilki = pd.read_csv(main_path_data + "\\vilki.csv")
    final2 = pd.read_csv(main_path_data + "\\all_data.csv")


    # sound = html.Div(id='hidden-div', style={"display": "none"})


    layout = [interval,
              # sound,
              dbc.Row(style={'padding':'0','margin':'0'},
                      children=[
                  dbc.Col(
                        style={'height': '93vh',
                               'max-height': '93vh',
                               'text-align': 'center',
                               'padding':'0',
                               'margin':'0',
                               'width':'60%',
                               'overflowY': "hidden"},
                        children=[

                            dbc.Row(style={'min-height': '40vh', 'max-height': '40vh',
                               'padding':'0',
                               'margin':'0',
                                           'overflowY': 'scroll'},
                                    children=[
                                        ddk.Card(style={
                                           'padding':'0',
                                           'margin':'0',
                                           'overflowY': 'hidden'},
                                            children=[
                                            dash_table.DataTable(
                                                id="table",
                                                data=vilki.to_dict('records'),
                                                columns=[{'id': c, 'name': c} for c in vilki.columns],
                                                sort_action='native',
                                                style_cell_conditional=[
                                                    {
                                                        'if': {'column_id': 'regim'},
                                                        'font-size': '11px',
                                                        'fontWeight': 'bold'
                                                    },
                                                    {
                                                        'if': {'column_id': 'timed'},
                                                        'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                    },
                                                    {
                                                        'if': {'column_id': 'b1'},
                                                        'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                        'padding':'0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'b2'},
                                                        'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'val1'},
                                                        'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'val2'},
                                                        'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'val3'},
                                                        'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'kurs1'},
                                                        'font-size': '12px',
                                                        'fontWeight': 'bold'
                                                    },
                                                    {
                                                        'if': {'column_id': 'kurs2'},
                                                        'font-size': '12px',
                                                        'fontWeight': 'bold'
                                                    },
                                                    {
                                                        'if': {'column_id': 'profit'},
                                                        'font-size': '12px',
                                                        'fontWeight': 'bold'
                                                    }




                                                    # {
                                                    #     'if': {'column_id': c},
                                                    #     'font-size': '9px',
                                                    #     'max-width': 'fit-content',
                                                    # } for c in
                                                    # ['regim', 'timed', 'b1', 'b2', 'val1', 'val2', 'val3',
                                                    #  'Go']
                                                ],
                                                style_data_conditional=[
                                                    {
                                                        'if': {'row_index': 'odd'},
                                                        'backgroundColor': 'rgb(248, 248, 248)'
                                                    },
                                                ],
                                                style_table={
                                                    'maxHeight': '100%',
                                                    'overflowY': 'scroll',
                                                    'width': '100%',
                                                    'minWidth': '100%',
                                                },
                                                style_cell={
                                                    'fontSize': '10px',
                                                    'fontFamily': 'Open Sans',
                                                    'textAlign': 'center',
                                                    'height': '30px',
                                                    'maxHeight': '30px',
                                                    'whiteSpace': 'inherit',
                                                    'overflow': 'hidden',
                                                    'textOverflow': 'ellipsis',
                                                },

                                                style_header={
                                                    'fontSize': '10px',
                                                    'backgroundColor': 'rgb(230, 230, 230)',
                                                    'fontWeight': 'bold'
                                                })
                                        ])
                                    ]),
                            dbc.Row(style={
                                # "width": "100%",
                                           'max-height': '58vh',
                                           'overflowY': 'scroll',
                               'padding':'0',
                               'margin':'0',
                                           },
                                    children=[

                                        ddk.Card(
                                            style={"width": "100%", 'min-height': '48vh', 'max-height': '48vh',
                               'padding':'0',
                               'margin':'0','margin-top':'10px',
                                                   'overflowY': 'scroll'},
                                            children=[dash_table.DataTable(
                                                id="table_all",
                                                data=final2.to_dict('records'),
                                                columns=[{'id': c, 'name': c} for c in final2.columns],
                                                # page_action='native',
                                                # filter_action='native',
                                                # filter_query='',
                                                # sort_action='native',
                                                # sort_mode='multi',
                                                # sort_by=[],
                                                export_format='xlsx',
                                                # export_headers='display',
                                                # merge_duplicate_headers=True,
                                                style_cell_conditional=[
                                                    {
                                                        'if': {'column_id': 'birga_x'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'birga_y'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'valin_x'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'valin_y'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'valout_x'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'res_birga1'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'overflow': 'hidden',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'res_birga2'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'overflow': 'hidden',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'TIME'},
                                                        # 'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                        'textOverflow': 'ellipsis',
                                                        'padding': '0',
                                                    },
                                                ],
                                                style_data_conditional=[
                                                    {
                                                        'if': {'row_index': 'odd'},
                                                        'backgroundColor': 'rgb(248, 248, 248)'
                                                    }
                                                ],
                                                style_table={
                                                    'maxHeight': '100%',
                                                    'overflowY': 'scroll',
                                                    'width': '100%',
                                                    'minWidth': '100%',
                                                },
                                                style_cell={
                                                    'fontSize': '10px',
                                                    'fontFamily': 'Open Sans',
                                                    'textAlign': 'center',
                                                    'height': '30px',
                                                    'maxHeight': '30px',
                                                    # 'width': '30px',
                                                    # 'maxWidth': '30px',
                                                    'padding': '0',
                                                    'whiteSpace': 'inherit',
                                                    'overflow': 'hidden',
                                                    # 'textOverflow': 'ellipsis',
                                                    # 'pd.options.display.float_format': '{:.5f}'.format,
                                                },
                                                style_header={
                                                    'fontSize': '10px',
                                                    'backgroundColor': 'rgb(230, 230, 230)',
                                                    'fontWeight': 'bold'
                                                }
                                            ),
                                            ])
                                        ]),
                            ]),
                  dbc.Col(
                        style={'height': '93vh',
                               'max-height': '93vh',
                               'text-align': 'center',
                               'padding':'0',
                               'margin':'0',
                               'max-width': '40%',
                               'width':'40%',
                       'overflowY': "hidden"},
                        children=[
                            dbc.Row(style={
                                # "width": "100%",
                                'min-height': '40vh', 'max-height': '40vh',
                               'padding':'0',
                               'margin':'0',
                                           'overflowY': 'hidden'},
                                    children=[
                                        ddk.Card(
                                            style={
                                                "width": "100%", 'min-height': '38vh', 'max-height': '38vh',
                                                   'padding':'0',
                                                   'margin':'0',
                                                   'overflowY': 'scroll'},
                                            children=[
                                                dash_table.DataTable(
                                                    id="valuta",
                                                    data=valuta.to_dict('records'),
                                                    columns=[{'id': c, 'name': c} for c in valuta.columns],
                                                    # page_action='native',
                                                    # filter_action='native',
                                                    # filter_query='',
                                                    # sort_action='native',
                                                    # sort_mode='multi',
                                                    # sort_by=[],
                                                    style_cell_conditional=[
                                                        {'if': {'column_id': 'Valuta'},
                                                         'fontWeight': 'bold',
                                                         'maxWidth': '30px',
                                                         'textOverflow': 'ellipsis',
                                                         },
                                                        {'if': {'column_id': 'Summa'},
                                                         'fontWeight': 'bold',
                                                         }
                                                    ],
                                                    style_data_conditional=[
                                                        {
                                                            'if': {'row_index': 'odd'},
                                                            'backgroundColor': 'rgb(248, 248, 248)'
                                                        }
                                                    ],
                                                    style_table={
                                                        'maxHeight': '100%',
                                                        'overflowY': 'scroll',
                                                        'width': '100%',
                                                        'minWidth': '100%',
                                                    },
                                                    style_cell={
                                                        'fontSize': '12px',
                                                        'fontFamily': 'Open Sans',
                                                        'textAlign': 'center',
                                                        'height': '15px',
                                                        'maxHeight': '20px',
                                                        'width': '30px',
                                                        # 'maxWidth': '30px',
                                                        # 'padding': '2px 22px',
                                                        'whiteSpace': 'inherit',
                                                        'overflow': 'hidden',
                                                        'textOverflow': 'ellipsis',
                                                    },
                                                    style_header={
                                                        'fontSize': '14px',
                                                        'backgroundColor': 'rgb(230, 230, 230)',
                                                        'fontWeight': 'bold'
                                                    }
                                                ),
                                            ]),

                                    ]),
                            dbc.Row(style={"width": "100%", 'min-height': '50vh', 'max-height': '50vh',
                                           'overflowY': 'scroll'},
                                    children=[
                                        dbc.Row(html.Div(
                                            # width=100,
                                            style={'padding-left': '0px'},
                                            children=[
                                                dbc.Row(
                                                    style={'margin': '0',
                                                           'padding': '0'},
                                                    children=[
                                                        dbc.Row(
                                                            style={'margin': '0',
                                                                   'margin-left': '10px',
                                                                   'padding': '0'},
                                                            children=[
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[
                                                                            dbc.Row(dcc.Dropdown(
                                                                                id='newbirga1_btn',
                                                                                style={'width': '100%',
                                                                                       'background-color': '#fff'},
                                                                                placeholder="БИРЖА 1",
                                                                                options=[
                                                                                    {
                                                                                        'label': 'alfa',
                                                                                        'value': 'alfa'},
                                                                                    {
                                                                                        'label': 'hot',
                                                                                        'value': 'hot'},
                                                                                    {
                                                                                        'label': 'live',
                                                                                        'value': 'live'},

                                                                                ],
                                                                                value='')),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='newbirga1_com_btn',
                                                                                placeholder="Комисия",
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[dbc.Row(dcc.Dropdown(
                                                                            id='newbirga2_btn',
                                                                            style={'width': '100%',
                                                                                   'background-color': '#fff'},
                                                                            placeholder="БИРЖА 2",
                                                                            options=[
                                                                                {
                                                                                    'label': 'alfa',
                                                                                    'value': 'alfa'},
                                                                                {
                                                                                    'label': 'hot',
                                                                                    'value': 'hot'},
                                                                                {
                                                                                    'label': 'live',
                                                                                    'value': 'live'},

                                                                            ],
                                                                            value='')),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='newbirga2_com_btn',
                                                                                placeholder="Комисия",
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[dbc.Row(dcc.Dropdown(
                                                                            id='newval1_btn',
                                                                            style={'width': '100%',
                                                                                   'background-color': '#fff'},
                                                                            options=[
                                                                                {'label': 'BTC',
                                                                                 'value': 'BTC'},
                                                                                {'label': 'USD',
                                                                                 'value': 'USD'},
                                                                                {'label': 'USDT',
                                                                                 'value': 'USDT'},
                                                                                {'label': 'ETH',
                                                                                 'value': 'ETH'},
                                                                                {'label': 'PZM',
                                                                                 'value': 'PZM'},

                                                                            ],
                                                                            value='', )),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='neworder_com_btn',
                                                                                placeholder="Минималка",
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[dbc.Row(dcc.Dropdown(
                                                                            id='newval2_btn',
                                                                            style={'width': '100%',
                                                                                   'background-color': '#fff'},
                                                                            options=[
                                                                                {'label': 'BTC',
                                                                                 'value': 'BTC'},
                                                                                {'label': 'USD',
                                                                                 'value': 'USD'},
                                                                                {'label': 'USDT',
                                                                                 'value': 'USDT'},
                                                                                {'label': 'ETH',
                                                                                 'value': 'ETH'},
                                                                                {'label': 'PZM',
                                                                                 'value': 'PZM'},

                                                                            ],
                                                                            value='')),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='newper_btn',
                                                                                placeholder="% ордера",
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[dbc.Row(dcc.Dropdown(
                                                                            id='newval3_btn',
                                                                            style={'width': '100%',
                                                                                   'background-color': '#fff'},
                                                                            options=[
                                                                                {'label': 'BTC',
                                                                                 'value': 'BTC'},
                                                                                {'label': 'USD',
                                                                                 'value': 'USD'},
                                                                                {'label': 'USDT',
                                                                                 'value': 'USDT'},
                                                                                {'label': 'ETH',
                                                                                 'value': 'ETH'},
                                                                                {'label': 'PZM',
                                                                                 'value': 'PZM'},

                                                                            ],
                                                                            value='')),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='newprofit_btn',
                                                                                placeholder='% профита',
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '25%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[html.Button('SAVE',
                                                                                              id='Create_NewRegim_btn',
                                                                                              n_clicks=0)]),

                                                            ])
                                                    ]
                                                )
                                            ])),
                                        dbc.Row(id="listcardreg",
                                                style={"width": "100%",
                                                       # 'min-height': '50vh',
                                                       # 'max-height': '45vh',
                                                       # 'overflowY': 'scroll'
                                                       },
                                                children=[i for i in MAIN_TAB.regims()])

                                    ])])

              ])
              ]

    return layout

def serve_layout2():
    interval = dcc.Interval(id='interval2', interval=1000, n_intervals=0)
    vilki2 = pd.read_csv(main_path_data + "\\vilki2.csv")
    vilki_all = pd.read_csv(main_path_data + "\\vilki2_all.csv")

    layout = [interval,
              dbc.Row(style={'padding':'0','margin':'0'},
                      children=[
                  dbc.Col(
                        style={'height': '93vh',
                               'max-height': '93vh',
                               'text-align': 'center',
                               'padding':'0',
                               'margin':'0',
                               'width':'60%',
                               'overflowY': "hidden"},
                        children=[

                            dbc.Row(style={'min-height': '40vh', 'max-height': '40vh',
                               'padding':'0',
                               'margin':'0',
                                           'overflowY': 'scroll'},
                                    children=[
                                        ddk.Card(style={
                                           'padding':'0',
                                           'margin':'0',
                                           'overflowY': 'hidden'},
                                            children=[
                                            dash_table.DataTable(
                                                id="vilki2_table",
                                                data=vilki2.to_dict('records'),
                                                columns=[{'id': c, 'name': c} for c in vilki2.columns],
                                                sort_action='native',
                                                style_cell_conditional=[
                                                    # {
                                                    #     'if': {'column_id': 'regim'},
                                                    #     'font-size': '11px',
                                                    #     'fontWeight': 'bold'
                                                    # },
                                                    # {
                                                    #     'if': {'column_id': 'timed'},
                                                    #     'font-size': '11px',
                                                    #     'max-width': 'fit-content',
                                                    # },
                                                    # {
                                                    #     'if': {'column_id': 'b1'},
                                                    #     'font-size': '11px',
                                                    #     'max-width': 'fit-content',
                                                    #     'padding':'0',
                                                    # },
                                                    # {
                                                    #     'if': {'column_id': 'b2'},
                                                    #     'font-size': '11px',
                                                    #     'max-width': 'fit-content',
                                                    #     'padding': '0',
                                                    # },
                                                    # {
                                                    #     'if': {'column_id': 'val1'},
                                                    #     'font-size': '11px',
                                                    #     'max-width': 'fit-content',
                                                    #     'padding': '0',
                                                    # },
                                                    # {
                                                    #     'if': {'column_id': 'val2'},
                                                    #     'font-size': '11px',
                                                    #     'max-width': 'fit-content',
                                                    #     'padding': '0',
                                                    # },
                                                    # {
                                                    #     'if': {'column_id': 'val3'},
                                                    #     'font-size': '11px',
                                                    #     'max-width': 'fit-content',
                                                    #     'padding': '0',
                                                    # },
                                                    # {
                                                    #     'if': {'column_id': 'kurs1'},
                                                    #     'font-size': '12px',
                                                    #     'fontWeight': 'bold'
                                                    # },
                                                    # {
                                                    #     'if': {'column_id': 'kurs2'},
                                                    #     'font-size': '12px',
                                                    #     'fontWeight': 'bold'
                                                    # },
                                                    # {
                                                    #     'if': {'column_id': 'profit'},
                                                    #     'font-size': '12px',
                                                    #     'fontWeight': 'bold'
                                                    # },
                                                    #

                                                    {
                                                        'if': {'column_id': c},
                                                        'display': 'none'
                                                    } for c in
                                                    ['direction_x','volume_x','Com_x','valin_y','direction_y','volume_y','Com_y','Bal1','Bal2','volume','profit','min_A','new_kurs','prof','per'
]
                                                ],
                                                style_data_conditional=[
                                                    {
                                                        'if': {'row_index': 'odd'},
                                                        'backgroundColor': 'rgb(248, 248, 248)'
                                                    },
                                                ],
                                                style_table={
                                                    'maxHeight': '100%',
                                                    'overflowY': 'scroll',
                                                    'width': '100%',
                                                    'minWidth': '100%',
                                                },
                                                style_cell={
                                                    'fontSize': '10px',
                                                    'fontFamily': 'Open Sans',
                                                    'textAlign': 'center',
                                                    'height': '30px',
                                                    'maxHeight': '30px',
                                                    'whiteSpace': 'inherit',
                                                    'overflow': 'hidden',
                                                    'textOverflow': 'ellipsis',
                                                },

                                                style_header={
                                                    'fontSize': '10px',
                                                    'backgroundColor': 'rgb(230, 230, 230)',
                                                    'fontWeight': 'bold'
                                                })
                                        ])
                                    ]),
                            dbc.Row(style={
                                # "width": "100%",
                                           'max-height': '58vh',
                                           'overflowY': 'scroll',
                               'padding':'0',
                               'margin':'0',
                                           },
                                    children=[

                                        ddk.Card(
                                            style={"width": "100%", 'min-height': '48vh', 'max-height': '48vh',
                               'padding':'0',
                               'margin':'0','margin-top':'10px',
                                                   'overflowY': 'scroll'},
                                            children=[dash_table.DataTable(
                                                id="vilki2_all_table",
                                                data=vilki_all.to_dict('records'),
                                                columns=[{'id': c, 'name': c} for c in vilki_all.columns],
                                                # page_action='native',
                                                # filter_action='native',
                                                # filter_query='',
                                                # sort_action='native',
                                                # sort_mode='multi',
                                                # sort_by=[],
                                                export_format='xlsx',
                                                # export_headers='display',
                                                # merge_duplicate_headers=True,
                                                style_cell_conditional=[
                                                    {
                                                        'if': {'column_id': 'birga_x'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'birga_y'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'valin_x'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'valin_y'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'valout_x'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'res_birga1'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'overflow': 'hidden',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'res_birga2'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'overflow': 'hidden',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'TIME'},
                                                        # 'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                        'textOverflow': 'ellipsis',
                                                        'padding': '0',
                                                    },
                                                ],
                                                style_data_conditional=[
                                                    {
                                                        'if': {'row_index': 'odd'},
                                                        'backgroundColor': 'rgb(248, 248, 248)'
                                                    }
                                                ],
                                                style_table={
                                                    'maxHeight': '100%',
                                                    'overflowY': 'scroll',
                                                    'width': '100%',
                                                    'minWidth': '100%',
                                                },
                                                style_cell={
                                                    'fontSize': '10px',
                                                    'fontFamily': 'Open Sans',
                                                    'textAlign': 'center',
                                                    'height': '30px',
                                                    'maxHeight': '30px',
                                                    # 'width': '30px',
                                                    # 'maxWidth': '30px',
                                                    'padding': '0',
                                                    'whiteSpace': 'inherit',
                                                    'overflow': 'hidden',
                                                    # 'textOverflow': 'ellipsis',
                                                    # 'pd.options.display.float_format': '{:.5f}'.format,
                                                },
                                                style_header={
                                                    'fontSize': '10px',
                                                    'backgroundColor': 'rgb(230, 230, 230)',
                                                    'fontWeight': 'bold'
                                                }
                                            ),
                                            ])
                                        ]),
                            ]),
                  dbc.Col(
                        style={'height': '93vh',
                               'max-height': '93vh',
                               'text-align': 'center',
                               'padding':'0',
                               'margin':'0',
                               'max-width': '40%',
                               'width':'40%',
                       'overflowY': "hidden"},
                        children=[
                            dbc.Row(style={"width": "100%", 'min-height': '90vh', 'max-height': '90vh',
                                           'overflowY': 'scroll'},
                                    children=[
                                        dbc.Row(html.Div(
                                            # width=100,
                                            style={'padding-left': '0px'},
                                            children=[
                                                dbc.Row(
                                                    style={'margin': '0',
                                                           'padding': '0'},
                                                    children=[
                                                        dbc.Row(
                                                            style={'margin': '0',
                                                                   'margin-left': '10px',
                                                                   'padding': '0'},
                                                            children=[
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[
                                                                            dbc.Row(dcc.Dropdown(
                                                                                id='newbirga1_btn_reg2',
                                                                                style={'width': '100%',
                                                                                       'background-color': '#fff'},
                                                                                placeholder="БИРЖА 1",
                                                                                options=[
                                                                                    {
                                                                                        'label': 'alfa',
                                                                                        'value': 'alfa'},
                                                                                    {
                                                                                        'label': 'hot',
                                                                                        'value': 'hot'},
                                                                                    {
                                                                                        'label': 'live',
                                                                                        'value': 'live'},

                                                                                ],
                                                                                value='')),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='newbirga1_com_btn_reg2',
                                                                                placeholder="Комисия",
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[dbc.Row(dcc.Dropdown(
                                                                            id='newbirga2_btn_reg2',
                                                                            style={'width': '100%',
                                                                                   'background-color': '#fff'},
                                                                            placeholder="БИРЖА 2",
                                                                            options=[
                                                                                {
                                                                                    'label': 'alfa',
                                                                                    'value': 'alfa'},
                                                                                {
                                                                                    'label': 'hot',
                                                                                    'value': 'hot'},
                                                                                {
                                                                                    'label': 'live',
                                                                                    'value': 'live'},

                                                                            ],
                                                                            value='')),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='newbirga2_com_btn_reg2',
                                                                                placeholder="Комисия",
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[dbc.Row(dcc.Dropdown(
                                                                            id='newval1_btn_reg2',
                                                                            style={'width': '100%',
                                                                                   'background-color': '#fff'},
                                                                            options=[
                                                                                {'label': 'BTC',
                                                                                 'value': 'BTC'},
                                                                                {'label': 'USD',
                                                                                 'value': 'USD'},
                                                                                {'label': 'USDT',
                                                                                 'value': 'USDT'},
                                                                                {'label': 'ETH',
                                                                                 'value': 'ETH'},
                                                                                {'label': 'PZM',
                                                                                 'value': 'PZM'},

                                                                            ],
                                                                            value='', )),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='neworder_com_btn_reg2',
                                                                                placeholder="Минималка",
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[dbc.Row(dcc.Dropdown(
                                                                            id='newval2_btn_reg2',
                                                                            style={'width': '100%',
                                                                                   'background-color': '#fff'},
                                                                            options=[
                                                                                {'label': 'BTC',
                                                                                 'value': 'BTC'},
                                                                                {'label': 'USD',
                                                                                 'value': 'USD'},
                                                                                {'label': 'USDT',
                                                                                 'value': 'USDT'},
                                                                                {'label': 'ETH',
                                                                                 'value': 'ETH'},
                                                                                {'label': 'PZM',
                                                                                 'value': 'PZM'},

                                                                            ],
                                                                            value='')),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='newper_btn_reg2',
                                                                                placeholder="% ордера",
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[dbc.Row(dcc.Dropdown(
                                                                            id='newval3_btn_reg2',
                                                                            style={'width': '100%',
                                                                                   'background-color': '#fff'},
                                                                            options=[
                                                                                {'label': 'BTC',
                                                                                 'value': 'BTC'},
                                                                                {'label': 'USD',
                                                                                 'value': 'USD'},
                                                                                {'label': 'USDT',
                                                                                 'value': 'USDT'},
                                                                                {'label': 'ETH',
                                                                                 'value': 'ETH'},
                                                                                {'label': 'PZM',
                                                                                 'value': 'PZM'},

                                                                            ],
                                                                            value='')),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='newprofit_btn_reg2',
                                                                                placeholder='% профита',
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '25%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[html.Button('SAVE',
                                                                                              id='Create_NewRegim_btn_reg2',
                                                                                              n_clicks=0)]),

                                                            ])
                                                    ]
                                                ),

                                        dbc.Row(id="listcardreg2",
                                                style={"width": "100%",
                                                       # 'min-height': '50vh',
                                                       # 'max-height': '45vh',
                                                       # 'overflowY': 'scroll'
                                                       },
                                                children=[i for i in MAIN_TAB.regims2()])
                                            ])),

                                    ])])

              ])
              ]

    return layout

def ring(i):
    if i == 0:
        return html.Audio(src='data:audio/mpeg;base64,{}'.format(encoded_sound.decode('utf-8')),
                   controls=False,
                   autoPlay=True,)
    else:
        return html.Div(id='ring', style={"display": "none"})

def sound(i):

    sound = html.Div(id='placeholder', style={"display": "none"}, children=ring(i))
    return sound

