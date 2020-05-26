import dash
import dash_core_components as dcc
import dash_html_components as html
from django_plotly_dash import DjangoDash

dash_structure = DjangoDash('home_dash')

dash_structure.layout = html.Div(id='main',
                                 children=[
                                     html.Div([html.Img(src='../static/c01.png', id='button_start', style={'display': 'block'}, n_clicks=0)]),
                                     html.Div([html.Img(src='../static/b01.png', id='button_save', style={'display': 'none'}, n_clicks=0)]),
                                     html.Div([html.Img(src='../static/b02.png', id='button_load', style={'display': 'none'}, n_clicks=0)]),
                                     html.Div([html.Img(src='../static/b04.png', id='button_up', style={'display': 'none'}, n_clicks=0)]),
                                     html.Div([html.Img(src='../static/b05.png', id='button_left', style={'display': 'none'}, n_clicks=0)]),
                                     html.Div([html.Img(src='../static/b07.png', id='button_right', style={'display': 'none'}, n_clicks=0)]),
                                     html.Div([html.Img(src='../static/b06.png', id='button_down', style={'display': 'none'}, n_clicks=0)]),
                                     html.Div([html.Img(src='../static/b08.png', id='button_enter', style={'display': 'none'}, n_clicks=0)]),
                                     html.Div([html.Img(src='../static/i41.png', id='tool_book', style={'display': 'none'}, n_clicks=0)]),
                                     html.Div([html.Img(src='../static/i31.png', id='tool_pickaxe', style={'display': 'none'}, n_clicks=0)]),
                                     html.Div([html.Img(src='../static/i32.png', id='tool_teleport', style={'display': 'none'}, n_clicks=0)]),
                                     html.Div([html.Img(src='../static/i13.png', id='tool_poison', style={'display': 'none'}, n_clicks=0)]),
                                     html.Div([html.Img(src='../static/i14.png', id='tool_doublehp', style={'display': 'none'}, n_clicks=0)]),
                                     html.Div([html.Img(src='../static/i42.png', id='tool_doubleg', style={'display': 'none'}, n_clicks=0)]),
                                     html.Div(id='tiles')])

#player initial data
#TOOL 0: BOOK 1: PICKAXE 2: TELEPORT 4: POISON 5: DOUBLE HP 6: DOUBLE GOLD
#TOOL 7: IRON SWORD 8: IRON SHIELD 9: STEEL SWORD 10: STEEL SHIELD
player_dict = {'POS':21113, 'POSF':1, 'HP':1000, 'LVL':1, 'XPHOLD':0, 'ATK':20, 'DEN':10, 'GHOLD':0, 'POI':0,
               'YKEY':0, 'BKEY':0, 'RKEY':0, 'TOOL':'10000000000', 'WBREAK':0, 'EVENT':'000', 'GOLDUP':1, 'XPUP':1,
               'FLOOR':'100000', 'DOOR':'000000000000000000000000000000',
               'ITEM':'0000000000000000000000000000000000000000000000000000000000000000000000000000000000',
               'MONSTER':'0000000000000000000000000000000000000000000000000000000'}

player_dict_save = {}

monster_dict = {'NAME':['Slime', 'Black Slime', 'Small Bat', 'Big Bat', 'Wizard', 'Red Wizard', 'Zombie', 'Zombie Ex',
                        'Skeleton', 'Sekelon Ex', 'Giant', 'Bat King', 'Wizard King', 'Demon King'],
                'HP':[50, 100, 80, 80, 100, 100, 120, 200, 150, 200, 50, 250, 300, 500],
                'ATK':[10, 12, 11, 11, 15, 15, 15, 15, 14, 19, 17, 20, 20, 100],
                'DEN':[5, 7, 6, 6, 0, 0, 7, 7, 10, 10, 15, 12, 15, 50],
                'SKL':[1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 3, 1, 1],
                'GDROP':[1, 3, 2, 4, 3, 5, 6, 7, 6, 8, 10, 20, 30, 50],
                'XPDROP':[1, 3, 2, 4, 3, 5, 6, 7, 6, 8, 10, 20, 30, 50],
                'PIC':['c11', 'c13', 'c21', 'c22', 'c26', 'c27', 'c31', 'c32', 'c36', 'c37', 'c41', 'c66', 'c67', 'c68']}

item_pos_dict = {0: '121302', 1: '120703', 2: '120803', 3: '121103', 4: '121503', 5: '121603', 6: '121104', 7: '121504', 8: '121604', 9: '120608',
                 10: '121711', 11: '120912', 12: '121712', 13: '120813', 14: '120913', 15: '121013', 16: '121513', 17: '121613', 18: '121713', 19: '221502',
                 20: '221602', 21: '221702', 22: '220703', 23: '221504', 24: '221604', 25: '221704', 26: '221006', 27: '220608', 28: '220808', 29: '220609',
                 30: '220809', 31: '221009', 32: '320902', 33: '321702', 34: '321703', 35: '321505', 36: '321705', 37: '321706', 38: '321707', 39: '321708',
                 40: '321709', 41: '321710', 42: '321011', 43: '321711', 44: '321012', 45: '321312', 46: '321412', 47: '321512', 48: '321712', 49: '321113',
                 50: '421202', 51: '421302', 52: '421402', 53: '421004', 54: '420808', 55: '420612', 56: '420712', 57: '421012', 58: '421212', 59: '421512',
                 60: '420613', 61: '420713', 62: '521002', 63: '521102', 64: '520606', 65: '521006', 66: '521106', 67: '520711', 68: '520811', 69: '520911',
                 70: '520712', 71: '520812', 72: '520912', 73: '521313', 74: '521713', 75: '621008', 76: '621108', 77: '621208', 78: '621009', 79: '621109',
                 80: '621209'}

door_pos_dict = {0: '120705', 1: '120908', 2: '121508', 3: '121110', 4: '120711', 5: '220903', 6: '221303', 7: '221403', 8: '221105', 9: '221705',
             10: '221109', 11: '221609', 12: '220711', 13: '321602', 14: '320810', 15: '321410', 16: '420605', 17: '421305', 18: '421107', 19: '420810',
             20: '421410', 21: '520803', 22: '521304', 23: '520805', 24: '521605', 25: '520809', 26: '521109', 27: '521410', 28: '521610'}

monster_pos_dict = {0: '120704', 1: '121105', 2:'121505', 3: '121606', 4: '120607', 5: '121107', 6: '121507', 7: '120708', 8: '120609', 9: '120812',
                    10: '120713', 11: '221203', 12: '221503', 13: '221603', 14: '221703', 15: '221104', 16: '221206', 17: '221306', 18: '221406', 19: '221308',
                    20: '221408', 21: '221209', 22: '221309', 23: '221409', 24: '221509', 25: '221310', 26: '221410', 27: '220612', 28: '220812', 29: '320903',
                    30: '321704', 31: '320805', 32: '321405', 33: '321406', 34: '321506', 35: '320807', 36: '321309', 37: '321509', 38: '320811', 39: '321111',
                    40: '321013', 41: '421603', 42: '421703', 43: '421306', 44: '420809', 45: '421010', 46: '421210', 47: '421113', 48: '520903', 49: '521604',
                    50: '520905', 51: '521111', 53: '521411', 54: '521611', 55: '621105'}

button_state = {'START':0, 'SAVE':0, 'LOAD':0, 'HELP':0, 'UP':0, 'LEFT':0, 'DOWN':0, 'RIGHT':0, 'ENTER':0, 'LOCK':0, 'SELECT': 0,
                'BOOK': 0, 'PICKAXE': 0, 'TELEPORT': 0, 'POISON': 0, 'HPDOUBLE': 0, 'GOLDDOUBLE': 0, 'GOLDUP': 0}

talk = {'conversation': '', 'selection1': '', 'selection2': ''}

def baserock_map():
    baserock = {
        'basepath':['../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png',
                    '../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png',
                    '../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png',
                    '../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png',
                    '../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png',
                    '../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png',
                    '../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png',
                    '../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png',
                    '../static/t10.png','../static/t10.png','../static/t10.png','../static/t10.png'],
        'baseid':['tile10501','tile10601','tile10701','tile10801','tile10901','tile11001','tile11101','tile11201','tile11301','tile11401',
                  'tile11501','tile11601','tile11701','tile11801','tile10502','tile11802','tile10503','tile11803','tile10504','tile11804',
                  'tile10505','tile11805','tile10506','tile11806','tile10507','tile11807','tile10508','tile11808','tile10509','tile11809',
                  'tile10510','tile11810','tile10511','tile11811','tile10512','tile11812','tile10513','tile11813','tile10514','tile10614',
                  'tile10714','tile10814','tile10914','tile11014','tile11114','tile11214','tile11314','tile11414','tile11514','tile11614',
                  'tile11714','tile11814']}
    return baserock

#base template, append everytime when callback
def template():
    tiledata_template = {
        'tilepath':['../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                    
                    '../static/c01.png','../static/i01.png','../static/i02.png','../static/i03.png'],
        'tileid':['tile10101','tile10201','tile10301','tile10401','tile11901','tile12001','tile12101','tile12201',
                  'tile10102','tile10202','tile10302','tile10402','tile11902','tile12002','tile12102','tile12202',
                  'tile10103','tile10203','tile10303','tile10403','tile11903','tile12003','tile12103','tile12203',
                  'tile10104','tile10204','tile10304','tile10404','tile11904','tile12004','tile12104','tile12204',
                  'tile10105','tile10205','tile10305','tile10405','tile11905','tile12005','tile12105','tile12205',
                  'tile10106','tile10206','tile10306','tile10406','tile11906','tile12006','tile12106','tile12206',
                  'tile10107','tile10207','tile10307','tile10407','tile11907','tile12007','tile12107','tile12207',
                  'tile10108','tile10208','tile10308','tile10408','tile11908','tile12008','tile12108','tile12208',
                  'tile10109','tile10209','tile10309','tile10409','tile11909','tile12009','tile12109','tile12209',
                  'tile10110','tile10210','tile10310','tile10410','tile11910','tile12010','tile12110','tile12210',
                  'tile10111','tile10211','tile10311','tile10411','tile11911','tile12011','tile12111','tile12211',
                  'tile10112','tile10212','tile10312','tile10412','tile11912','tile12012','tile12112','tile12212',
                  'tile10113','tile10213','tile10313','tile10413','tile11913','tile12013','tile12113','tile12213',
                  'tile10114','tile10214','tile10314','tile10414','tile11914','tile12014','tile12114','tile12214',
                  
                  'tile_icon','tile_yellow','tile_blue','tile_red']}
    children = []
    baserock = baserock_map()
    for k in range(len(baserock['basepath'])):
        children.append(html.Div([html.Img(src=baserock['basepath'][k], id=baserock['baseid'][k])]))
    for k in range(len(tiledata_template['tilepath'])):
        children.append(html.Div([html.Img(src=tiledata_template['tilepath'][k], id=tiledata_template['tileid'][k])]))
    return children

def floor_map(floor):
    if floor == 1:
        floor_map = {
            'tilepath':['../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t41.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        
                        '../static/i01.png','../static/i01.png','../static/i11.png','../static/i52.png','../static/i01.png','../static/i02.png',
                        '../static/c11.png','../static/i02.png','../static/i01.png','../static/i11.png','../static/t21.png','../static/c11.png',
                        '../static/c26.png','../static/c11.png','../static/c11.png','../static/c11.png','../static/c11.png','../static/i11.png',
                        '../static/c11.png','../static/t21.png','../static/t21.png','../static/c11.png','../static/t21.png','../static/t22.png',
                        '../static/i51.png','../static/c31.png','../static/i12.png','../static/i01.png','../static/c36.png','../static/i12.png',
                        '../static/i01.png','../static/c71.png','../static/i11.png','../static/i01.png','../static/i02.png'],
            
            'tileid':['tile10602','tile10702','tile10802','tile10902','tile11002','tile11102','tile11202','tile11302','tile11402',
                      'tile11502','tile11602','tile11702',
                      'tile10603','tile10703','tile10803','tile10903','tile11003','tile11103','tile11203','tile11303','tile11403',
                      'tile11503','tile11603','tile11703',
                      'tile10604','tile10704','tile10804','tile10904','tile11004','tile11104','tile11204','tile11304','tile11404',
                      'tile11504','tile11604','tile11704',
                      'tile10605','tile10705','tile10805','tile10905','tile11005','tile11105','tile11205','tile11305','tile11405',
                      'tile11505','tile11605','tile11705',
                      'tile10606','tile10706','tile10806','tile10906','tile11006','tile11106','tile11206','tile11306','tile11406',
                      'tile11506','tile11606','tile11706',
                      'tile10607','tile10707','tile10807','tile10907','tile11007','tile11107','tile11207','tile11307','tile11407',
                      'tile11507','tile11607','tile11707',
                      'tile10608','tile10708','tile10808','tile10908','tile11008','tile11108','tile11208','tile11308','tile11408',
                      'tile11508','tile11608','tile11708',
                      'tile10609','tile10709','tile10809','tile10909','tile11009','tile11109','tile11209','tile11309','tile11409',
                      'tile11509','tile11609','tile11709',
                      'tile10610','tile10710','tile10810','tile10910','tile11010','tile11110','tile11210','tile11310','tile11410',
                      'tile11510','tile11610','tile11710',
                      'tile10611','tile10711','tile10811','tile10911','tile11011','tile11111','tile11211','tile11311','tile11411',
                      'tile11511','tile11611','tile11711',
                      'tile10612','tile10712','tile10812','tile10912','tile11012','tile11112','tile11212','tile11312','tile11412',
                      'tile11512','tile11612','tile11712',
                      'tile10613','tile10713','tile10813','tile10913','tile11013','tile11113','tile11213','tile11313','tile11413',
                      'tile11513','tile11613','tile11713',
                      
                      'tile20602','tile20702','tile20802','tile20902','tile21202','tile21402','tile21502','tile21602','tile21702',
                      'tile20603','tile20903','tile21203','tile21403','tile21703','tile20604','tile20904','tile21204','tile21404',
                      'tile21704','tile20605','tile20805','tile20905','tile21405','tile21705','tile20906','tile21006','tile21106',
                      'tile21206','tile21406','tile21706','tile20907','tile21407','tile21707','tile21208','tile21408','tile21608',
                      'tile21708','tile20909','tile21209','tile20910','tile21010','tile21210','tile21310','tile21410','tile21610',
                      'tile21710','tile20611','tile20811','tile20911','tile21011','tile21311','tile21411','tile20612','tile21012',
                      'tile21312','tile21412','tile20613','tile21013','tile21313','tile21413',
                      
                      'tile21302','tile20703','tile20803','tile21103','tile21503','tile21603','tile20704','tile21104','tile21504',
                      'tile21604','tile20705','tile21105','tile21505','tile21606','tile20607','tile21107','tile21507','tile20608',
                      'tile20708','tile20908','tile21508','tile20609','tile21110','tile20711','tile21711','tile20812','tile20912',
                      'tile21712','tile20713','tile20813','tile20913','tile21213','tile21513','tile21613','tile21713']}
        
        floor_map_new = dict(floor_map)
        for i in range(0, 11):
            if player_dict['MONSTER'][i].find('1') > -1:    
                monster_pos_query = monster_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(monster_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        for i in range(0, 19):
            if player_dict['ITEM'][i].find('1') > -1:    
                item_pos_query = item_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(item_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        for i in range(0, 5):
            if player_dict['DOOR'][i].find('1') > -1:    
                door_pos_query = door_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(door_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        if player_dict['WBREAK'] != 0:
            path_query = list(floor_map.values())[1].index('tile{}'.format(player_dict['WBREAK']))
            del floor_map_new['tilepath'][path_query]
            del floor_map_new['tileid'][path_query]
    
    elif floor == 2:
        floor_map = {
            'tilepath':['../static/t41.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t42.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png','../static/t11.png',
                        
                        '../static/i11.png','../static/i11.png','../static/i01.png','../static/i21.png','../static/t22.png','../static/c21.png',
                        '../static/t21.png','../static/t21.png','../static/c21.png','../static/c21.png','../static/c22.png','../static/c13.png',
                        '../static/i11.png','../static/i11.png','../static/i01.png','../static/t22.png','../static/t21.png','../static/c76.png',
                        '../static/c77.png','../static/c78.png','../static/i12.png','../static/c21.png','../static/c26.png','../static/c21.png',
                        '../static/i51.png','../static/i51.png','../static/c21.png','../static/c11.png','../static/i52.png','../static/i52.png',
                        '../static/i23.png','../static/t22.png','../static/c27.png','../static/c36.png','../static/c36.png','../static/c13.png',
                        '../static/t21.png','../static/c21.png','../static/c11.png','../static/t24.png','../static/c41.png','../static/c41.png',
                        '../static/c71.png'],
            
            'tileid':['tile10602','tile10702','tile10802','tile10902','tile11002','tile11102','tile11202','tile11302','tile11402',
                      'tile11502','tile11602','tile11702',
                      'tile10603','tile10703','tile10803','tile10903','tile11003','tile11103','tile11203','tile11303','tile11403',
                      'tile11503','tile11603','tile11703',
                      'tile10604','tile10704','tile10804','tile10904','tile11004','tile11104','tile11204','tile11304','tile11404',
                      'tile11504','tile11604','tile11704',
                      'tile10605','tile10705','tile10805','tile10905','tile11005','tile11105','tile11205','tile11305','tile11405',
                      'tile11505','tile11605','tile11705',
                      'tile10606','tile10706','tile10806','tile10906','tile11006','tile11106','tile11206','tile11306','tile11406',
                      'tile11506','tile11606','tile11706',
                      'tile10607','tile10707','tile10807','tile10907','tile11007','tile11107','tile11207','tile11307','tile11407',
                      'tile11507','tile11607','tile11707',
                      'tile10608','tile10708','tile10808','tile10908','tile11008','tile11108','tile11208','tile11308','tile11408',
                      'tile11508','tile11608','tile11708',
                      'tile10609','tile10709','tile10809','tile10909','tile11009','tile11109','tile11209','tile11309','tile11409',
                      'tile11509','tile11609','tile11709',
                      'tile10610','tile10710','tile10810','tile10910','tile11010','tile11110','tile11210','tile11310','tile11410',
                      'tile11510','tile11610','tile11710',
                      'tile10611','tile10711','tile10811','tile10911','tile11011','tile11111','tile11211','tile11311','tile11411',
                      'tile11511','tile11611','tile11711',
                      'tile10612','tile10712','tile10812','tile10912','tile11012','tile11112','tile11212','tile11312','tile11412',
                      'tile11512','tile11612','tile11712',
                      'tile10613','tile10713','tile10813','tile10913','tile11013','tile11113','tile11213','tile11313','tile11413',
                      'tile11513','tile11613','tile11713',
                      
                      'tile20902','tile21302','tile21402','tile20904','tile21304','tile21404','tile20605','tile20705','tile20805',
                      'tile20905','tile21005','tile21205','tile21305','tile21405','tile21505','tile21605','tile20906','tile20907',
                      'tile21007','tile21107','tile21207','tile21307','tile21407','tile21507','tile21607','tile20908','tile21108',
                      'tile21608','tile20909','tile20910','tile21110','tile21610','tile20611','tile20811','tile20911','tile21111',
                      'tile21211','tile21311','tile21411','tile21511','tile21611','tile20912','tile21012','tile21112',
                      
                      'tile21502','tile21602','tile21702','tile20703','tile20903','tile21203','tile21303','tile21403','tile21503',
                      'tile21603','tile21703','tile21104','tile21504','tile21604','tile21704','tile21105','tile21705','tile20606',
                      'tile20706','tile20806','tile21006','tile21206','tile21306','tile21406','tile20608','tile20808','tile21308',
                      'tile21408','tile20609','tile20809','tile21009','tile21109','tile21209','tile21309','tile21409','tile21509',
                      'tile21609','tile21310','tile21410','tile20711','tile20612','tile20812','tile21212']}
        
        floor_map_new = dict(floor_map)
        for i in range(11, 29):
            if player_dict['MONSTER'][i].find('1') > -1:    
                monster_pos_query = monster_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(monster_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        for i in range(19, 32):
            if player_dict['ITEM'][i].find('1') > -1:    
                item_pos_query = item_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(item_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        for i in range(5, 13):
            if player_dict['DOOR'][i].find('1') > -1:    
                door_pos_query = door_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(door_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        if player_dict['WBREAK'] != 0:
            path_query = list(floor_map.values())[1].index('tile{}'.format(player_dict['WBREAK']))
            del floor_map_new['tilepath'][path_query]
            del floor_map_new['tileid'][path_query]
        
    elif floor == 3:
        floor_map = {
            'tilepath':['../static/t42.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t01.png','../static/t41.png',
                        
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        
                        '../static/i51.png','../static/t23.png','../static/i11.png','../static/c36.png','../static/i12.png','../static/c66.png',
                        '../static/c13.png','../static/c31.png','../static/i13.png','../static/i51.png','../static/c36.png','../static/c27.png',
                        '../static/i52.png','../static/c13.png','../static/i01.png','../static/i01.png','../static/c41.png','../static/c41.png',
                        '../static/i01.png','../static/t21.png','../static/t24.png','../static/i02.png','../static/c21.png','../static/i11.png',
                        '../static/c22.png','../static/i02.png','../static/i01.png','../static/i03.png','../static/i12.png','../static/i32.png',
                        '../static/i02.png','../static/c22.png','../static/i12.png'],
            
            'tileid':['tile10602','tile10702','tile10802','tile10902','tile11002','tile11102','tile11202','tile11302','tile11402',
                      'tile11502','tile11602','tile11702',
                      'tile10603','tile10703','tile10803','tile10903','tile11003','tile11103','tile11203','tile11303','tile11403',
                      'tile11503','tile11603','tile11703',
                      'tile10604','tile10704','tile10804','tile10904','tile11004','tile11104','tile11204','tile11304','tile11404',
                      'tile11504','tile11604','tile11704',
                      'tile10605','tile10705','tile10805','tile10905','tile11005','tile11105','tile11205','tile11305','tile11405',
                      'tile11505','tile11605','tile11705',
                      'tile10606','tile10706','tile10806','tile10906','tile11006','tile11106','tile11206','tile11306','tile11406',
                      'tile11506','tile11606','tile11706',
                      'tile10607','tile10707','tile10807','tile10907','tile11007','tile11107','tile11207','tile11307','tile11407',
                      'tile11507','tile11607','tile11707',
                      'tile10608','tile10708','tile10808','tile10908','tile11008','tile11108','tile11208','tile11308','tile11408',
                      'tile11508','tile11608','tile11708',
                      'tile10609','tile10709','tile10809','tile10909','tile11009','tile11109','tile11209','tile11309','tile11409',
                      'tile11509','tile11609','tile11709',
                      'tile10610','tile10710','tile10810','tile10910','tile11010','tile11110','tile11210','tile11310','tile11410',
                      'tile11510','tile11610','tile11710',
                      'tile10611','tile10711','tile10811','tile10911','tile11011','tile11111','tile11211','tile11311','tile11411',
                      'tile11511','tile11611','tile11711',
                      'tile10612','tile10712','tile10812','tile10912','tile11012','tile11112','tile11212','tile11312','tile11412',
                      'tile11512','tile11612','tile11712',
                      'tile10613','tile10713','tile10813','tile10913','tile11013','tile11113','tile11213','tile11313','tile11413',
                      'tile11513','tile11613','tile11713',
                      
                      'tile20802','tile21002','tile21202','tile20803','tile21003','tile21403','tile21603','tile20704','tile20804',
                      'tile21004','tile21204','tile21304','tile21404','tile21504','tile21604','tile21005','tile21605','tile20606',
                      'tile20706','tile20806','tile21006','tile21206','tile21606','tile21007','tile21207','tile21607','tile20708',
                      'tile20808','tile20908','tile21008','tile21208','tile21608','tile21209','tile21609','tile20610','tile20710',
                      'tile20910','tile21010','tile21210','tile21310','tile21510','tile21610','tile20611','tile20911','tile21211',
                      'tile21611','tile20612','tile20912','tile21112','tile21212','tile21612','tile20613','tile20713','tile20813',
                      'tile20913','tile21213','tile21313','tile21413','tile21513','tile21613',
                      
                      'tile20902','tile21602','tile21702','tile20903','tile21703','tile21704','tile20805','tile21405','tile21505',
                      'tile21705','tile21406','tile21506','tile21706','tile20807','tile21707','tile21708','tile21309','tile21509',
                      'tile21709','tile20810','tile21410','tile21710','tile20811','tile21011','tile21111','tile21711','tile21012',
                      'tile21312','tile21412','tile21512','tile21712','tile21013','tile21113']}
        
        floor_map_new = dict(floor_map)
        for i in range(29, 41):
            if player_dict['MONSTER'][i].find('1') > -1:    
                monster_pos_query = monster_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(monster_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        for i in range(32, 50):
            if player_dict['ITEM'][i].find('1') > -1:    
                item_pos_query = item_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(item_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        for i in range(13, 16):
            if player_dict['DOOR'][i].find('1') > -1:    
                door_pos_query = door_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(door_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
    
    elif floor == 4:
        floor_map = {
            'tilepath':['../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t41.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t42.png',
                        
                        '../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png',
                        '../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png',
                        '../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png',
                        '../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png',
                        '../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png',
                        '../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png',
                        '../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png',
                        '../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png','../static/t12.png',
                        
                        '../static/c76.png','../static/c77.png','../static/c78.png','../static/i01.png','../static/i42.png','../static/i01.png',
                        '../static/c32.png','../static/c31.png','../static/i12.png','../static/t21.png','../static/t21.png','../static/c37.png',
                        '../static/c73.png','../static/t22.png','../static/i11.png','../static/c36.png','../static/t22.png','../static/c26.png',
                        '../static/c26.png','../static/t22.png','../static/i01.png','../static/i01.png','../static/i12.png','../static/i51.png',
                        '../static/i31.png','../static/i03.png','../static/i01.png','../static/c27.png'],
            
            'tileid':['tile10602','tile10702','tile10802','tile10902','tile11002','tile11102','tile11202','tile11302','tile11402',
                      'tile11502','tile11602','tile11702',
                      'tile10603','tile10703','tile10803','tile10903','tile11003','tile11103','tile11203','tile11303','tile11403',
                      'tile11503','tile11603','tile11703',
                      'tile10604','tile10704','tile10804','tile10904','tile11004','tile11104','tile11204','tile11304','tile11404',
                      'tile11504','tile11604','tile11704',
                      'tile10605','tile10705','tile10805','tile10905','tile11005','tile11105','tile11205','tile11305','tile11405',
                      'tile11505','tile11605','tile11705',
                      'tile10606','tile10706','tile10806','tile10906','tile11006','tile11106','tile11206','tile11306','tile11406',
                      'tile11506','tile11606','tile11706',
                      'tile10607','tile10707','tile10807','tile10907','tile11007','tile11107','tile11207','tile11307','tile11407',
                      'tile11507','tile11607','tile11707',
                      'tile10608','tile10708','tile10808','tile10908','tile11008','tile11108','tile11208','tile11308','tile11408',
                      'tile11508','tile11608','tile11708',
                      'tile10609','tile10709','tile10809','tile10909','tile11009','tile11109','tile11209','tile11309','tile11409',
                      'tile11509','tile11609','tile11709',
                      'tile10610','tile10710','tile10810','tile10910','tile11010','tile11110','tile11210','tile11310','tile11410',
                      'tile11510','tile11610','tile11710',
                      'tile10611','tile10711','tile10811','tile10911','tile11011','tile11111','tile11211','tile11311','tile11411',
                      'tile11511','tile11611','tile11711',
                      'tile10612','tile10712','tile10812','tile10912','tile11012','tile11112','tile11212','tile11312','tile11412',
                      'tile11512','tile11612','tile11712',
                      'tile10613','tile10713','tile10813','tile10913','tile11013','tile11113','tile11213','tile11313','tile11413',
                      'tile11513','tile11613','tile11713',
                      
                      'tile21102','tile21502','tile21103','tile21503','tile21104','tile21504','tile20705','tile20805','tile20905',
                      'tile21005','tile21105','tile21205','tile21405','tile21505','tile21605','tile21106','tile20707','tile20807',
                      'tile20907','tile20908','tile21108','tile21308','tile21408','tile21508','tile21608','tile20909','tile21109',
                      'tile21309','tile20610','tile20710','tile20910','tile21109','tile21310','tile21510','tile21610','tile20911',
                      'tile21111','tile21311','tile21611','tile20912','tile21112','tile21312','tile21612','tile20913','tile21313',
                      'tile21413','tile21513','tile21613',
                      
                      'tile20702','tile20802','tile20902','tile21202','tile21302','tile21402','tile21603','tile21703','tile21004',
                      'tile20605','tile21305','tile21306','tile21506','tile21107','tile20808','tile20809','tile20810','tile21010',
                      'tile21210','tile21410','tile20612','tile20712','tile21012','tile21212','tile21512','tile20613','tile20713',
                      'tile21113']}
        
        floor_map_new = dict(floor_map)
        for i in range(41, 48):
            if player_dict['MONSTER'][i].find('1') > -1:    
                monster_pos_query = monster_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(monster_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        for i in range(50, 62):
            if player_dict['ITEM'][i].find('1') > -1:    
                item_pos_query = item_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(item_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        for i in range(16, 21):
            if player_dict['DOOR'][i].find('1') > -1:    
                door_pos_query = door_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(door_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
    
    elif floor == 5:
        floor_map = {
            'tilepath':['../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t42.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t03.png','../static/t02.png',
                        '../static/t03.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t03.png','../static/t02.png',
                        '../static/t03.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t03.png','../static/t02.png',
                        '../static/t03.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t03.png','../static/t02.png',
                        '../static/t03.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        '../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t03.png','../static/t41.png',
                        '../static/t03.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png','../static/t02.png',
                        
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png','../static/t13.png',
                        '../static/t13.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png','../static/t11.png',
                        '../static/t11.png',
                        
                        '../static/c72.png','../static/i01.png','../static/i11.png','../static/c71.png','../static/t21.png','../static/c32.png',
                        '../static/t21.png','../static/c37.png','../static/t22.png','../static/c31.png','../static/t21.png','../static/i14.png',
                        '../static/i02.png','../static/i12.png','../static/t22.png','../static/t23.png','../static/t21.png','../static/t21.png',
                        '../static/i51.png','../static/i52.png','../static/i01.png','../static/c67.png','../static/c32.png','../static/c32.png',
                        '../static/i52.png','../static/i51.png','../static/i02.png','../static/i22.png','../static/i24.png',],
            
            'tileid':['tile10602','tile10702','tile10802','tile10902','tile11002','tile11102','tile11202','tile11302','tile11402',
                      'tile11502','tile11602','tile11702',
                      'tile10603','tile10703','tile10803','tile10903','tile11003','tile11103','tile11203','tile11303','tile11403',
                      'tile11503','tile11603','tile11703',
                      'tile10604','tile10704','tile10804','tile10904','tile11004','tile11104','tile11204','tile11304','tile11404',
                      'tile11504','tile11604','tile11704',
                      'tile10605','tile10705','tile10805','tile10905','tile11005','tile11105','tile11205','tile11305','tile11405',
                      'tile11505','tile11605','tile11705',
                      'tile10606','tile10706','tile10806','tile10906','tile11006','tile11106','tile11206','tile11306','tile11406',
                      'tile11506','tile11606','tile11706',
                      'tile10607','tile10707','tile10807','tile10907','tile11007','tile11107','tile11207','tile11307','tile11407',
                      'tile11507','tile11607','tile11707',
                      'tile10608','tile10708','tile10808','tile10908','tile11008','tile11108','tile11208','tile11308','tile11408',
                      'tile11508','tile11608','tile11708',
                      'tile10609','tile10709','tile10809','tile10909','tile11009','tile11109','tile11209','tile11309','tile11409',
                      'tile11509','tile11609','tile11709',
                      'tile10610','tile10710','tile10810','tile10910','tile11010','tile11110','tile11210','tile11310','tile11410',
                      'tile11510','tile11610','tile11710',
                      'tile10611','tile10711','tile10811','tile10911','tile11011','tile11111','tile11211','tile11311','tile11411',
                      'tile11511','tile11611','tile11711',
                      'tile10612','tile10712','tile10812','tile10912','tile11012','tile11112','tile11212','tile11312','tile11412',
                      'tile11512','tile11612','tile11712',
                      'tile10613','tile10713','tile10813','tile10913','tile11013','tile11113','tile11213','tile11313','tile11413',
                      'tile11513','tile11613','tile11713',
                      
                      'tile20802','tile21302','tile21502','tile21303','tile21503','tile20704','tile20804','tile20904','tile21004',
                      'tile21104','tile21504','tile21305','tile21505','tile21705','tile20806','tile21306','tile20607','tile20807',
                      'tile20907','tile21007','tile21107','tile21207','tile21307','tile20609','tile20709','tile20909','tile20610',
                      'tile21510','tile20611','tile21511','tile20612','tile21512','tile20613','tile20713','tile20813','tile20913',
                      'tile21513','tile21308','tile21408','tile21608','tile21708','tile21310','tile21710',
                      
                      'tile20602','tile21002','tile21102','tile21402','tile20803','tile20903','tile21304','tile21604','tile20805',
                      'tile20905','tile21605','tile20606','tile21006','tile21106','tile20809','tile21109','tile21410','tile21610',
                      'tile20711','tile20811','tile20911','tile21111','tile21411','tile21611','tile20712','tile20812','tile20912',
                      'tile21313','tile21713']}
        
        floor_map_new = dict(floor_map)
        for i in range(48, 54):
            if player_dict['MONSTER'][i].find('1') > -1:    
                monster_pos_query = monster_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(monster_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        for i in range(62, 75):
            if player_dict['ITEM'][i].find('1') > -1:    
                item_pos_query = item_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(item_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        for i in range(21, 29):
            if player_dict['DOOR'][i].find('1') > -1:    
                door_pos_query = door_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(door_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        if player_dict['WBREAK'] != 0:
            path_query = list(floor_map.values())[1].index('tile{}'.format(player_dict['WBREAK']))
            del floor_map_new['tilepath'][path_query]
            del floor_map_new['tileid'][path_query]
    
    elif floor == 6:
        floor_map = {
            'tilepath':['../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t01.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t01.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t01.png','../static/t01.png',
                        '../static/t01.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t01.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t01.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png',
                        '../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png','../static/t04.png',
                        
                        '../static/c75.png','../static/c68.png','../static/i12.png','../static/i12.png','../static/i12.png','../static/i11.png',
                        '../static/i11.png','../static/i11.png'],
            
            'tileid':['tile10602','tile10702','tile10802','tile10902','tile11002','tile11102','tile11202','tile11302','tile11402',
                      'tile11502','tile11602','tile11702',
                      'tile10603','tile10703','tile10803','tile10903','tile11003','tile11103','tile11203','tile11303','tile11403',
                      'tile11503','tile11603','tile11703',
                      'tile10604','tile10704','tile10804','tile10904','tile11004','tile11104','tile11204','tile11304','tile11404',
                      'tile11504','tile11604','tile11704',
                      'tile10605','tile10705','tile10805','tile10905','tile11005','tile11105','tile11205','tile11305','tile11405',
                      'tile11505','tile11605','tile11705',
                      'tile10606','tile10706','tile10806','tile10906','tile11006','tile11106','tile11206','tile11306','tile11406',
                      'tile11506','tile11606','tile11706',
                      'tile10607','tile10707','tile10807','tile10907','tile11007','tile11107','tile11207','tile11307','tile11407',
                      'tile11507','tile11607','tile11707',
                      'tile10608','tile10708','tile10808','tile10908','tile11008','tile11108','tile11208','tile11308','tile11408',
                      'tile11508','tile11608','tile11708',
                      'tile10609','tile10709','tile10809','tile10909','tile11009','tile11109','tile11209','tile11309','tile11409',
                      'tile11509','tile11609','tile11709',
                      'tile10610','tile10710','tile10810','tile10910','tile11010','tile11110','tile11210','tile11310','tile11410',
                      'tile11510','tile11610','tile11710',
                      'tile10611','tile10711','tile10811','tile10911','tile11011','tile11111','tile11211','tile11311','tile11411',
                      'tile11511','tile11611','tile11711',
                      'tile10612','tile10712','tile10812','tile10912','tile11012','tile11112','tile11212','tile11312','tile11412',
                      'tile11512','tile11612','tile11712',
                      'tile10613','tile10713','tile10813','tile10913','tile11013','tile11113','tile11213','tile11313','tile11413',
                      'tile11513','tile11613','tile11713',
                      
                      'tile21102','tile21106','tile21008','tile21108','tile21208','tile21009','tile21109','tile21209']}
        
        floor_map_new = dict(floor_map)
        for i in range(54, 55):
            if player_dict['MONSTER'][i].find('1') > -1:    
                monster_pos_query = monster_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(monster_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        for i in range(75, 81):
            if player_dict['ITEM'][i].find('1') > -1:    
                item_pos_query = item_pos_dict[i]
                path_query = list(floor_map.values())[1].index('tile{}'.format(item_pos_query[1:]))
                del floor_map_new['tilepath'][path_query]
                del floor_map_new['tileid'][path_query]
        
    return floor_map_new

def youshallnotpass(pos_new):
    sound = ''
    if button_state['LOCK'] == 0:
        player_pos_new = 'tile{}'.format(pos_new)
        tiledata = floor_map(player_dict['POSF'])
        if player_pos_new in list(tiledata.values())[1]:
            path_query = list(tiledata.values())[0][list(tiledata.values())[1].index(player_pos_new)]
            playerid = 'tile{}'.format(player_dict['POS'])
            if path_query[-7:-5] == 'c7': #npc EVENT
                event_list = list(player_dict['EVENT'])
                if pos_new == 21213:
                    if event_list[0] == '0':
                        event_list[0] = '1'
                        player_dict.update({'EVENT': ''.join(event_list), 'YKEY': player_dict['YKEY'] + 1})
                        talk.update({'conversation': 'Here is a Yellow Key (Click Okay)'})
                        button_state.update({'LOCK':3})
                    else:
                        talk.update({'conversation': 'Have a good trip! (Click Okay)'})
                        button_state.update({'LOCK':3})
                elif pos_new == 21212:
                    talk.update({'conversation': 'Win two guards to open that door (Click Okay)'})
                    button_state.update({'LOCK':3})
                elif pos_new == 21506:
                    talk.update({'conversation': 'Pickaxe can destroy wooden wall (Click Okay)'})
                    button_state.update({'LOCK':3})
                elif pos_new == 20602:
                    if event_list[1] == '0':
                        event_list[1] = '1'
                        talk.update({'conversation': 'Use 50 GOLD to buy 1 blue key',
                                     'selection1': 'Buy (Click Okay)', 'selection2': 'Not Buy (Click Okay)'})
                        button_state.update({'LOCK':1, 'SELECT': 1})
                    else:
                        talk.update({'conversation': 'You cannot buy anymore (Click Okay)'})
                        button_state.update({'LOCK':3})
                elif pos_new == 21402:
                    talk.update({'conversation': 'Think about using the pickaxe? (Click Okay)'})
                    button_state.update({'LOCK':3})
                elif pos_new == 21102:
                    talk.update({'conversation': 'You saved me! (The End)'})
                    button_state.update({'LOCK':4})
                    sound = 'ending'
                elif pos_new == 20706:
                    talk.update({'conversation': 'Spend {} GOLD to upgrade'.format(player_dict['GOLDUP'] * 20),
                                     'selection1': 'Increase 3 ATK and 3 DEF (Click Okay)', 'selection2': 'Do not upgrade (Click Okay)'})
                    button_state.update({'LOCK':1, 'SELECT': 2})
                elif pos_new == 20802:
                    talk.update({'conversation': 'Spend {} EXP EXP to upgrade'.format(player_dict['XPUP'] * 40),
                                     'selection1': 'Increase 1 LVL (Click Okay)', 'selection2': 'Do not upgrade (Click Okay)'})
                    button_state.update({'LOCK':1, 'SELECT': 3})
            elif path_query[-7:-5] == 't2': #door EVENT
                if path_query[-5:-4] == '1':
                    if player_dict['YKEY'] > 0:
                        door_list = list(player_dict['DOOR'])
                        door_pos_query = list(door_pos_dict.keys())[list(door_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                        door_list[door_pos_query] = '1'
                        player_dict.update({'DOOR': ''.join(door_list), 'YKEY': player_dict['YKEY'] - 1})
                        sound = 'door'
                elif path_query[-5:-4] == '2':
                    if player_dict['BKEY'] > 0:
                        door_list = list(player_dict['DOOR'])
                        door_pos_query = list(door_pos_dict.keys())[list(door_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                        door_list[door_pos_query] = '1'
                        player_dict.update({'DOOR': ''.join(door_list), 'BKEY': player_dict['BKEY'] - 1})
                        sound = 'door'
                elif path_query[-5:-4] == '3':
                    if player_dict['RKEY'] > 0:
                        door_list = list(player_dict['DOOR'])
                        door_pos_query = list(door_pos_dict.keys())[list(door_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                        door_list[door_pos_query] = '1'
                        player_dict.update({'DOOR': ''.join(door_list), 'RKEY': player_dict['RKEY'] - 1})
                        sound = 'door'
                elif path_query[-5:-4] == '4':
                    if player_dict['POSF'] == 2:
                        if player_dict['MONSTER'][27] == '1' and player_dict['MONSTER'][28] == '1':
                            door_list = list(player_dict['DOOR'])
                            door_pos_query = list(door_pos_dict.keys())[list(door_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                            door_list[door_pos_query] = '1'
                            player_dict.update({'DOOR': ''.join(door_list)})
                            sound = 'door'
                    elif player_dict['POSF'] == 3:
                        if player_dict['MONSTER'][36] == '1' and player_dict['MONSTER'][37] == '1':
                            door_list = list(player_dict['DOOR'])
                            door_pos_query = list(door_pos_dict.keys())[list(door_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                            door_list[door_pos_query] = '1'
                            player_dict.update({'DOOR': ''.join(door_list)})
                            sound = 'door'
            elif path_query[-7:-6] == 'i': #item EVENT
                if path_query[-6:-4] == '01':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'YKEY': player_dict['YKEY'] + 1})
                elif path_query[-6:-4] == '02':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'BKEY': player_dict['BKEY'] + 1})
                elif path_query[-6:-4] == '03':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'RKEY': player_dict['RKEY'] + 1})
                elif path_query[-6:-4] == '11':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'HP': player_dict['HP'] + 50})
                elif path_query[-6:-4] == '12':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'HP': player_dict['HP'] + 200})
                elif path_query[-6:-4] == '13':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    tool_list = list(player_dict['TOOL'])
                    tool_list[4] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'TOOL': ''.join(tool_list)})
                elif path_query[-6:-4] == '14':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    tool_list = list(player_dict['TOOL'])
                    tool_list[5] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'TOOL': ''.join(tool_list)})
                elif path_query[-6:-4] == '21':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    tool_list = list(player_dict['TOOL'])
                    tool_list[7] = '1'
                    tool_list[8] = '0'
                    player_dict.update({'ITEM': ''.join(item_list), 'TOOL': ''.join(tool_list), 'ATK': player_dict['ATK'] + 10})
                elif path_query[-6:-4] == '22':
                    item_list = list(player_dict['ITEM'])
                    tool_list = list(player_dict['TOOL'])
                    tool_list[9] = '1'
                    tool_list[10] = '0'
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'TOOL': ''.join(tool_list), 'ATK': player_dict['ATK'] + 20})
                elif path_query[-6:-4] == '23':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    tool_list = list(player_dict['TOOL'])
                    tool_list[7] = '0'
                    tool_list[8] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'TOOL': ''.join(tool_list), 'ATK': player_dict['DEN'] + 10})
                elif path_query[-6:-4] == '24':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    tool_list = list(player_dict['TOOL'])
                    tool_list[9] = '0'
                    tool_list[10] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'TOOL': ''.join(tool_list), 'ATK': player_dict['DEN'] + 20})
                elif path_query[-6:-4] == '31':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    tool_list = list(player_dict['TOOL'])
                    tool_list[1] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'TOOL': ''.join(tool_list)})
                elif path_query[-6:-4] == '32':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    tool_list = list(player_dict['TOOL'])
                    tool_list[2] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'TOOL': ''.join(tool_list)})
                elif path_query[-6:-4] == '42':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    tool_list = list(player_dict['TOOL'])
                    tool_list[6] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'TOOL': ''.join(tool_list)})
                elif path_query[-6:-4] == '51':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'ATK': player_dict['ATK'] + 2})
                elif path_query[-6:-4] == '52':
                    item_list = list(player_dict['ITEM'])
                    item_query = list(item_pos_dict.keys())[list(item_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                    item_list[item_query] = '1'
                    player_dict.update({'ITEM': ''.join(item_list), 'DEN': player_dict['DEN'] + 2})
            elif path_query[-7:-6] == 'c': #fight EVENT
                player_hp = player_dict['HP']
                player_atk = player_dict['ATK']
                player_den = player_dict['DEN']
                path_query = list(tiledata.values())[0][list(tiledata.values())[1].index(player_pos_new)]
                monster_query = list(monster_dict.values())[7].index(path_query[-7:-4])
                monster_hp = list(monster_dict.values())[1][monster_query]
                monster_atk = list(monster_dict.values())[2][monster_query]
                monster_den = list(monster_dict.values())[3][monster_query]
                monster_skill = list(monster_dict.values())[4][monster_query]
                if player_atk < monster_den:
                    player_atk = 0
                if monster_atk < player_den:
                    monster_atk = 0
                
                while player_hp > 0:
                    monster_hp -= player_atk - monster_den
                    if monster_hp <= 0:
                        monster_pos_list = list(player_dict['MONSTER'])
                        monster_pos_query = list(monster_pos_dict.keys())[list(monster_pos_dict.values()).index(str(player_dict['POSF']) + str(pos_new))]
                        monster_pos_list[monster_pos_query] = '1'
                        if monster_skill == 3:
                            player_dict.update({'POI': 1})
                        if player_dict['TOOL'][6] == '1':
                            ghold = player_dict['GHOLD'] + list(monster_dict.values())[5][monster_query] * 2
                        else:
                            ghold = player_dict['GHOLD'] + list(monster_dict.values())[5][monster_query]
                        xphold = player_dict['XPHOLD'] + list(monster_dict.values())[6][monster_query]
                        player_dict.update({'HP': player_hp, 'GHOLD': ghold, 'XPHOLD': xphold, 'MONSTER': ''.join(monster_pos_list)})
                        break
                    else:
                        if monster_skill == 2:
                            player_hp -= (monster_atk - player_den) * 2
                            sound = 'fight2'
                        else:
                            player_hp -= monster_atk - player_den
                            sound = 'fight1'
                    if player_hp <= 0:
                        player_dict.update({'HP': player_hp})
                        talk.update({'conversation': 'You lose, load data or refresh to restart',
                                     'selection1': 'Load (Click Okay)'})
                        button_state.update({'LOCK':5})
                        sound = 'lose'
        else:
            tile_pos_new = 'tile{}'.format(pos_new - 10000)
            baserock = baserock_map()
            if tile_pos_new in list(baserock.values())[1]: #baserock
                playerid = 'tile{}'.format(player_dict['POS'])
            else:
                path_query = list(tiledata.values())[0][list(tiledata.values())[1].index(tile_pos_new)]
                if path_query[-6:-4] == '01' or path_query[-6:-4] == '02': #ground or ice
                    playerid = 'tile{}'.format(pos_new)
                    player_dict.update({'POS': pos_new})
                    if player_dict['POI'] == 1 and player_dict['HP'] > 50:
                        player_dict.update({'HP': player_dict['HP'] - 50})
                elif path_query[-6:-4] == '41': #up stair EVENT
                    playerid = 'tile{}'.format(pos_new)
                    newfloor = player_dict['POSF'] + 1
                    player_dict.update({'POS': pos_new, 'POSF': newfloor})
                    if player_dict['FLOOR'][newfloor - 1] == '0':
                        floor_list = list(player_dict['FLOOR'])
                        floor_list[newfloor - 1] = '1'
                        player_dict.update({'FLOOR': ''.join(floor_list)})
                        if player_dict['POI'] == 1 and player_dict['HP'] > 50:
                            player_dict.update({'HP': player_dict['HP'] - 50})
                        sound = 'stair'
                elif path_query[-6:-4] == '42': #down stair EVENT
                    playerid = 'tile{}'.format(pos_new)
                    newfloor = player_dict['POSF'] - 1
                    player_dict.update({'POS': pos_new, 'POSF': newfloor})
                    if player_dict['FLOOR'][newfloor - 1] == '0':
                        floor_list = list(player_dict['FLOOR'])
                        floor_list[newfloor - 1] = '1'
                        player_dict.update({'FLOOR': ''.join(floor_list)})
                        if player_dict['POI'] == 1 and player_dict['HP'] > 50:
                            player_dict.update({'HP': player_dict['HP'] - 50})
                        sound = 'stair'
                else: #sea or lava
                     playerid = 'tile{}'.format(player_dict['POS'])
    else:
        playerid = 'tile{}'.format(player_dict['POS'])
    playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
    return playerdata, sound

@dash_structure.expanded_callback(
    [dash.dependencies.Output('tiles','children'),dash.dependencies.Output('button_start','style'),dash.dependencies.Output('button_save','style'),
     dash.dependencies.Output('button_load','style'),dash.dependencies.Output('button_up','style'),dash.dependencies.Output('button_left','style'),
     dash.dependencies.Output('button_down','style'),dash.dependencies.Output('button_right','style'),dash.dependencies.Output('button_enter','style'),
     dash.dependencies.Output('tool_book','style'),dash.dependencies.Output('tool_pickaxe','style'),dash.dependencies.Output('tool_teleport','style'),
     dash.dependencies.Output('tool_poison','style'),dash.dependencies.Output('tool_doublehp','style'),dash.dependencies.Output('tool_doubleg','style')],
    [dash.dependencies.Input('button_start','n_clicks'),dash.dependencies.Input('button_save','n_clicks'),dash.dependencies.Input('button_load','n_clicks'),
     dash.dependencies.Input('button_up','n_clicks'),dash.dependencies.Input('button_left','n_clicks'),dash.dependencies.Input('button_down','n_clicks'),
     dash.dependencies.Input('button_right','n_clicks'),dash.dependencies.Input('button_enter','n_clicks'),dash.dependencies.Input('tool_book','n_clicks'),
     dash.dependencies.Input('tool_pickaxe','n_clicks'),dash.dependencies.Input('tool_teleport','n_clicks'),dash.dependencies.Input('tool_poison','n_clicks'),
     dash.dependencies.Input('tool_doublehp','n_clicks'),],
    [dash.dependencies.State('tiles','children')])

def display(n_cli_start, n_cli_save, n_cli_load, n_cli_up, n_cli_left, n_cli_down, n_cli_right, n_cli_enter,
            n_cli_book, n_cli_pick, n_cli_tel, n_cli_poi, n_cli_hpd, existing_state, **kwargs):
    if n_cli_start > button_state['START']:
        playerid = 'tile{}'.format(player_dict['POS'])
        playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
        
        children = template()
        tiledata = floor_map(player_dict['POSF'])
        if player_dict['POI'] == 1:
            status = 'Poison'
        else:
            status = 'Normal'
        textdata = {'text':['{}F'.format(player_dict['POSF']),status,player_dict['LVL'],player_dict['HP'],player_dict['ATK'],player_dict['DEN'],
                            player_dict['GHOLD'],player_dict['XPHOLD'],player_dict['YKEY'],player_dict['BKEY'],player_dict['RKEY']],
                    'textid':['var_floor','var_status','var_lvl','var_hp','var_atk','var_den','var_ghold','var_xphold','var_ykey','var_bkey','var_rkey']}
        
        for k in range(len(tiledata['tilepath'])):
            children.append(html.Div([html.Img(src=tiledata['tilepath'][k], id=tiledata['tileid'][k])]))
        for k in range(len(textdata['text'])):
            children.append(html.Div([html.H4(textdata['text'][k], id=textdata['textid'][k])]))
        textdata_template = {
            'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Save','Load','Up','Left','Right','Down','Okay'],
            'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield',
                  'text_save','text_load','text_up','text_left','text_right','text_down','text_enter']}
        for k in range(len(textdata_template['text'])):
            children.append(html.Div([html.H4(textdata_template['text'][k], id=textdata_template['textid'][k])]))
        children.append(html.Div([html.Img(src=playerdata['playerpath'][0], id=playerdata['playerid'][0])]))
        
        button_state.update({'START': n_cli_start})
        sty_start = {'display': 'none'}
        sty_img = {'display': 'block'}
        sty_select = {'display': 'block'}
        sty_enter = {'display': 'block'}
        sty_book = {'display': 'block'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
        
        children.append(html.Div([html.Audio(src='../static/opening.mp3', autoPlay='autoPlay')]))
    
    elif n_cli_up > button_state['UP']:
        children = template()
        playerid = 'tile{}'.format(player_dict['POS'])
        playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
        
        if button_state['LOCK'] == 0:
            pos_new = player_dict['POS'] - 1
            playerdata, sound = youshallnotpass(pos_new)
        
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection1'))
        elif button_state['LOCK'] == 3 or button_state['LOCK'] == 4:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
        elif button_state['LOCK'] == 5:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div(id='selection1'))
        
        tiledata = floor_map(player_dict['POSF'])
        if player_dict['POI'] == 1:
            status = 'Poison'
        else:
            status = 'Normal'
        textdata = {'text':['{}F'.format(player_dict['POSF']),status,player_dict['LVL'],player_dict['HP'],player_dict['ATK'],player_dict['DEN'],
                            player_dict['GHOLD'],player_dict['XPHOLD'],player_dict['YKEY'],player_dict['BKEY'],player_dict['RKEY']],
                    'textid':['var_floor','var_status','var_lvl','var_hp','var_atk','var_den','var_ghold','var_xphold','var_ykey','var_bkey','var_rkey']}
        
        for k in range(len(tiledata['tilepath'])):
            children.append(html.Div([html.Img(src=tiledata['tilepath'][k], id=tiledata['tileid'][k])]))
        for k in range(len(textdata['text'])):
            children.append(html.Div([html.H4(textdata['text'][k], id=textdata['textid'][k])]))
        children.append(html.Div([html.Img(src=playerdata['playerpath'][0], id=playerdata['playerid'][0])]))
        
        sty_img = {'display': 'block'}
        sty_select = {'display': 'block'}
        sty_enter = {'display': 'block'}
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Up','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_up','text_down','text_enter']}
            sty_img = {'display': 'none'}
        elif button_state['LOCK'] == 3:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        elif button_state['LOCK'] == 0:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Save','Load','Up','Left','Right','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield',
                      'text_save','text_load','text_up','text_left','text_right','text_down','text_enter']}
        elif button_state['LOCK'] == 4:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
            sty_enter = {'display': 'none'}
        elif button_state['LOCK'] == 5:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        for k in range(len(textdata_template['text'])):
            children.append(html.Div([html.H4(textdata_template['text'][k], id=textdata_template['textid'][k])]))
        if player_dict['TOOL'][7] == '1':
            if player_dict['TOOL'][9] == '1':
                children.append(html.Div([html.Img(src='../static/i22.png', id='tool_sword')]))
            else:
                children.append(html.Div([html.Img(src='../static/i21.png', id='tool_sword')]))
        if player_dict['TOOL'][8] == '1':
            if player_dict['TOOL'][10] == '1':
                children.append(html.Div([html.Img(src='../static/i24.png', id='tool_shield')]))
            else:
                children.append(html.Div([html.Img(src='../static/i23.png', id='tool_shield')]))
        
        button_state.update({'UP': n_cli_up})
        sty_start = {'display': 'none'}
        sty_book = {'display': 'block'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
        if player_dict['TOOL'][1] == '1':
            sty_pick = {'display': 'block'}
        if player_dict['TOOL'][2] == '1':
            sty_tel = {'display': 'block'}
        if player_dict['TOOL'][4] == '1':
            sty_poi = {'display': 'block'}
        if player_dict['TOOL'][5] == '1':
            sty_hpd = {'display': 'block'}
        if player_dict['TOOL'][6] == '1':
            sty_god = {'display': 'block'}
        
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            children.append(html.Div([html.Audio(src='../static/select.mp3', autoPlay='autoPlay')]))
        elif len(sound) > 0:
            children.append(html.Div([html.Audio(src='../static/{}.mp3'.format(sound), autoPlay='autoPlay')]))
    
    elif n_cli_left > button_state['LEFT']:
        children = template()
        playerid = 'tile{}'.format(player_dict['POS'])
        playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
        
        if button_state['LOCK'] == 0:
            pos_new = player_dict['POS'] - 100
            playerdata, sound = youshallnotpass(pos_new)
        
        if button_state['LOCK'] == 1:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection1'))
        elif button_state['LOCK'] == 2:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection2'))
        elif button_state['LOCK'] == 3 or button_state['LOCK'] == 4:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
        elif button_state['LOCK'] == 5:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div(id='selection1'))
        
        tiledata = floor_map(player_dict['POSF'])
        if player_dict['POI'] == 1:
            status = 'Poison'
        else:
            status = 'Normal'
        textdata = {'text':['{}F'.format(player_dict['POSF']),status,player_dict['LVL'],player_dict['HP'],player_dict['ATK'],player_dict['DEN'],
                            player_dict['GHOLD'],player_dict['XPHOLD'],player_dict['YKEY'],player_dict['BKEY'],player_dict['RKEY']],
                    'textid':['var_floor','var_status','var_lvl','var_hp','var_atk','var_den','var_ghold','var_xphold','var_ykey','var_bkey','var_rkey']}
        
        for k in range(len(tiledata['tilepath'])):
            children.append(html.Div([html.Img(src=tiledata['tilepath'][k], id=tiledata['tileid'][k])]))
        for k in range(len(textdata['text'])):
            children.append(html.Div([html.H4(textdata['text'][k], id=textdata['textid'][k])]))
        children.append(html.Div([html.Img(src=playerdata['playerpath'][0], id=playerdata['playerid'][0])]))
        
        sty_img = {'display': 'block'}
        sty_select = {'display': 'block'}
        sty_enter = {'display': 'block'}
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Up','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_up','text_down','text_enter']}
            sty_img = {'display': 'none'}
        elif button_state['LOCK'] == 3:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        elif button_state['LOCK'] == 0:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Save','Load','Up','Left','Right','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield',
                      'text_save','text_load','text_up','text_left','text_right','text_down','text_enter']}
        elif button_state['LOCK'] == 4:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
            sty_enter = {'display': 'none'}
        elif button_state['LOCK'] == 5:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        for k in range(len(textdata_template['text'])):
            children.append(html.Div([html.H4(textdata_template['text'][k], id=textdata_template['textid'][k])]))
        if player_dict['TOOL'][7] == '1':
            if player_dict['TOOL'][9] == '1':
                children.append(html.Div([html.Img(src='../static/i22.png', id='tool_sword')]))
            else:
                children.append(html.Div([html.Img(src='../static/i21.png', id='tool_sword')]))
        if player_dict['TOOL'][8] == '1':
            if player_dict['TOOL'][10] == '1':
                children.append(html.Div([html.Img(src='../static/i24.png', id='tool_shield')]))
            else:
                children.append(html.Div([html.Img(src='../static/i23.png', id='tool_shield')]))
        
        button_state.update({'LEFT': n_cli_left})
        sty_start = {'display': 'none'}
        sty_book = {'display': 'block'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
        if player_dict['TOOL'][1] == '1':
            sty_pick = {'display': 'block'}
        if player_dict['TOOL'][2] == '1':
            sty_tel = {'display': 'block'}
        if player_dict['TOOL'][4] == '1':
            sty_poi = {'display': 'block'}
        if player_dict['TOOL'][5] == '1':
            sty_hpd = {'display': 'block'}
        if player_dict['TOOL'][6] == '1':
            sty_god = {'display': 'block'}
        
        if len(sound) > 0:
            children.append(html.Div([html.Audio(src='../static/{}.mp3'.format(sound), autoPlay='autoPlay')]))
    
    elif n_cli_down > button_state['DOWN']:
        children = template()
        playerid = 'tile{}'.format(player_dict['POS'])
        playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
        
        if button_state['LOCK'] == 0:
            pos_new = player_dict['POS'] + 1
            playerdata, sound = youshallnotpass(pos_new)
        
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection2'))
            button_state.update({'LOCK':2})
        elif button_state['LOCK'] == 3 or button_state['LOCK'] == 4:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
        elif button_state['LOCK'] == 5:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div(id='selection1'))
        
        tiledata = floor_map(player_dict['POSF'])
        if player_dict['POI'] == 1:
            status = 'Poison'
        else:
            status = 'Normal'
        textdata = {'text':['{}F'.format(player_dict['POSF']),status,player_dict['LVL'],player_dict['HP'],player_dict['ATK'],player_dict['DEN'],
                            player_dict['GHOLD'],player_dict['XPHOLD'],player_dict['YKEY'],player_dict['BKEY'],player_dict['RKEY']],
                    'textid':['var_floor','var_status','var_lvl','var_hp','var_atk','var_den','var_ghold','var_xphold','var_ykey','var_bkey','var_rkey']}
        
        for k in range(len(tiledata['tilepath'])):
            children.append(html.Div([html.Img(src=tiledata['tilepath'][k], id=tiledata['tileid'][k])]))
        for k in range(len(textdata['text'])):
            children.append(html.Div([html.H4(textdata['text'][k], id=textdata['textid'][k])]))
        children.append(html.Div([html.Img(src=playerdata['playerpath'][0], id=playerdata['playerid'][0])]))
        
        sty_img = {'display': 'block'}
        sty_select = {'display': 'block'}
        sty_enter = {'display': 'block'}
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Up','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_up','text_down','text_enter']}
            sty_img = {'display': 'none'}
        elif button_state['LOCK'] == 3:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        elif button_state['LOCK'] == 0:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Save','Load','Up','Left','Right','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield',
                      'text_save','text_load','text_up','text_left','text_right','text_down','text_enter']}
        elif button_state['LOCK'] == 4:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
            sty_enter = {'display': 'none'}
        elif button_state['LOCK'] == 5:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        for k in range(len(textdata_template['text'])):
            children.append(html.Div([html.H4(textdata_template['text'][k], id=textdata_template['textid'][k])]))
        if player_dict['TOOL'][7] == '1':
            if player_dict['TOOL'][9] == '1':
                children.append(html.Div([html.Img(src='../static/i22.png', id='tool_sword')]))
            else:
                children.append(html.Div([html.Img(src='../static/i21.png', id='tool_sword')]))
        if player_dict['TOOL'][8] == '1':
            if player_dict['TOOL'][10] == '1':
                children.append(html.Div([html.Img(src='../static/i24.png', id='tool_shield')]))
            else:
                children.append(html.Div([html.Img(src='../static/i23.png', id='tool_shield')]))
        
        button_state.update({'DOWN': n_cli_down})
        sty_start = {'display': 'none'}
        sty_book = {'display': 'block'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
        if player_dict['TOOL'][1] == '1':
            sty_pick = {'display': 'block'}
        if player_dict['TOOL'][2] == '1':
            sty_tel = {'display': 'block'}
        if player_dict['TOOL'][4] == '1':
            sty_poi = {'display': 'block'}
        if player_dict['TOOL'][5] == '1':
            sty_hpd = {'display': 'block'}
        if player_dict['TOOL'][6] == '1':
            sty_god = {'display': 'block'}
        
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            children.append(html.Div([html.Audio(src='../static/select.mp3', autoPlay='autoPlay')]))
        elif len(sound) > 0:
            children.append(html.Div([html.Audio(src='../static/{}.mp3'.format(sound), autoPlay='autoPlay')]))
    
    elif n_cli_right > button_state['RIGHT']:
        children = template()
        playerid = 'tile{}'.format(player_dict['POS'])
        playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
        
        if button_state['LOCK'] == 0:
            pos_new = player_dict['POS'] + 100
            playerdata, sound = youshallnotpass(pos_new)
        
        if button_state['LOCK'] == 1:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection1'))
        elif button_state['LOCK'] == 2:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection2'))
        elif button_state['LOCK'] == 3 or button_state['LOCK'] == 4:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
        elif button_state['LOCK'] == 5:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div(id='selection1'))
        
        tiledata = floor_map(player_dict['POSF'])
        if player_dict['POI'] == 1:
            status = 'Poison'
        else:
            status = 'Normal'
        textdata = {'text':['{}F'.format(player_dict['POSF']),status,player_dict['LVL'],player_dict['HP'],player_dict['ATK'],player_dict['DEN'],
                            player_dict['GHOLD'],player_dict['XPHOLD'],player_dict['YKEY'],player_dict['BKEY'],player_dict['RKEY']],
                    'textid':['var_floor','var_status','var_lvl','var_hp','var_atk','var_den','var_ghold','var_xphold','var_ykey','var_bkey','var_rkey']}
        
        for k in range(len(tiledata['tilepath'])):
            children.append(html.Div([html.Img(src=tiledata['tilepath'][k], id=tiledata['tileid'][k])]))
        for k in range(len(textdata['text'])):
            children.append(html.Div([html.H4(textdata['text'][k], id=textdata['textid'][k])]))
        children.append(html.Div([html.Img(src=playerdata['playerpath'][0], id=playerdata['playerid'][0])]))
        
        sty_img = {'display': 'block'}
        sty_select = {'display': 'block'}
        sty_enter = {'display': 'block'}
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Up','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_up','text_down','text_enter']}
            sty_img = {'display': 'none'}
        elif button_state['LOCK'] == 3:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        elif button_state['LOCK'] == 0:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Save','Load','Up','Left','Right','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield',
                      'text_save','text_load','text_up','text_left','text_right','text_down','text_enter']}
        elif button_state['LOCK'] == 4:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
            sty_enter = {'display': 'none'}
        elif button_state['LOCK'] == 5:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        for k in range(len(textdata_template['text'])):
            children.append(html.Div([html.H4(textdata_template['text'][k], id=textdata_template['textid'][k])]))
        if player_dict['TOOL'][7] == '1':
            if player_dict['TOOL'][9] == '1':
                children.append(html.Div([html.Img(src='../static/i22.png', id='tool_sword')]))
            else:
                children.append(html.Div([html.Img(src='../static/i21.png', id='tool_sword')]))
        if player_dict['TOOL'][8] == '1':
            if player_dict['TOOL'][10] == '1':
                children.append(html.Div([html.Img(src='../static/i24.png', id='tool_shield')]))
            else:
                children.append(html.Div([html.Img(src='../static/i23.png', id='tool_shield')]))
        
        button_state.update({'RIGHT': n_cli_right})
        sty_start = {'display': 'none'}
        sty_book = {'display': 'block'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
        if player_dict['TOOL'][1] == '1':
            sty_pick = {'display': 'block'}
        if player_dict['TOOL'][2] == '1':
            sty_tel = {'display': 'block'}
        if player_dict['TOOL'][4] == '1':
            sty_poi = {'display': 'block'}
        if player_dict['TOOL'][5] == '1':
            sty_hpd = {'display': 'block'}
        if player_dict['TOOL'][6] == '1':
            sty_god = {'display': 'block'}
        
        if len(sound) > 0:
            children.append(html.Div([html.Audio(src='../static/{}.mp3'.format(sound), autoPlay='autoPlay')]))
    
    elif n_cli_poi > button_state['POISON']:
        children = template()
        playerid = 'tile{}'.format(player_dict['POS'])
        playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
        
        if button_state['LOCK'] == 0:
            if player_dict['POI'] == 1:
                tool_list = list(player_dict['TOOL'])
                tool_list[4] = '0'
                player_dict.update({'POI': 0, 'TOOL': ''.join(tool_list)})
        
        if button_state['LOCK'] == 1:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection1'))
        elif button_state['LOCK'] == 2:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection2'))
        elif button_state['LOCK'] == 3 or button_state['LOCK'] == 4:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
        elif button_state['LOCK'] == 5:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div(id='selection1'))
        
        tiledata = floor_map(player_dict['POSF'])
        if player_dict['POI'] == 1:
            status = 'Poison'
        else:
            status = 'Normal'
        textdata = {'text':['{}F'.format(player_dict['POSF']),status,player_dict['LVL'],player_dict['HP'],player_dict['ATK'],player_dict['DEN'],
                            player_dict['GHOLD'],player_dict['XPHOLD'],player_dict['YKEY'],player_dict['BKEY'],player_dict['RKEY']],
                    'textid':['var_floor','var_status','var_lvl','var_hp','var_atk','var_den','var_ghold','var_xphold','var_ykey','var_bkey','var_rkey']}
        
        for k in range(len(tiledata['tilepath'])):
            children.append(html.Div([html.Img(src=tiledata['tilepath'][k], id=tiledata['tileid'][k])]))
        for k in range(len(textdata['text'])):
            children.append(html.Div([html.H4(textdata['text'][k], id=textdata['textid'][k])]))
        children.append(html.Div([html.Img(src=playerdata['playerpath'][0], id=playerdata['playerid'][0])]))
        
        sty_img = {'display': 'block'}
        sty_select = {'display': 'block'}
        sty_enter = {'display': 'block'}
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Up','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_up','text_down','text_enter']}
            sty_img = {'display': 'none'}
        elif button_state['LOCK'] == 3:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        elif button_state['LOCK'] == 0:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Save','Load','Up','Left','Right','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield',
                      'text_save','text_load','text_up','text_left','text_right','text_down','text_enter']}
        elif button_state['LOCK'] == 4:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
            sty_enter = {'display': 'none'}
        elif button_state['LOCK'] == 5:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        for k in range(len(textdata_template['text'])):
            children.append(html.Div([html.H4(textdata_template['text'][k], id=textdata_template['textid'][k])]))
        if player_dict['TOOL'][7] == '1':
            if player_dict['TOOL'][9] == '1':
                children.append(html.Div([html.Img(src='../static/i22.png', id='tool_sword')]))
            else:
                children.append(html.Div([html.Img(src='../static/i21.png', id='tool_sword')]))
        if player_dict['TOOL'][8] == '1':
            if player_dict['TOOL'][10] == '1':
                children.append(html.Div([html.Img(src='../static/i24.png', id='tool_shield')]))
            else:
                children.append(html.Div([html.Img(src='../static/i23.png', id='tool_shield')]))
        
        button_state.update({'POISON': n_cli_poi})
        sty_start = {'display': 'none'}
        sty_book = {'display': 'block'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
        if player_dict['TOOL'][1] == '1':
            sty_pick = {'display': 'block'}
        if player_dict['TOOL'][2] == '1':
            sty_tel = {'display': 'block'}
        if player_dict['TOOL'][4] == '1':
            sty_poi = {'display': 'block'}
        if player_dict['TOOL'][5] == '1':
            sty_hpd = {'display': 'block'}
        if player_dict['TOOL'][6] == '1':
            sty_god = {'display': 'block'}
    
    elif n_cli_hpd > button_state['HPDOUBLE']:
        children = template()
        playerid = 'tile{}'.format(player_dict['POS'])
        playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
        
        if button_state['LOCK'] == 0:
            tool_list = list(player_dict['TOOL'])
            tool_list[5] = '0'
            player_dict.update({'HP': player_dict['HP'] * 2, 'TOOL': ''.join(tool_list)})
        
        if button_state['LOCK'] == 1:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection1'))
        elif button_state['LOCK'] == 2:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection2'))
        elif button_state['LOCK'] == 3 or button_state['LOCK'] == 4:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
        elif button_state['LOCK'] == 5:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div(id='selection1'))
        
        tiledata = floor_map(player_dict['POSF'])
        if player_dict['POI'] == 1:
            status = 'Poison'
        else:
            status = 'Normal'
        textdata = {'text':['{}F'.format(player_dict['POSF']),status,player_dict['LVL'],player_dict['HP'],player_dict['ATK'],player_dict['DEN'],
                            player_dict['GHOLD'],player_dict['XPHOLD'],player_dict['YKEY'],player_dict['BKEY'],player_dict['RKEY']],
                    'textid':['var_floor','var_status','var_lvl','var_hp','var_atk','var_den','var_ghold','var_xphold','var_ykey','var_bkey','var_rkey']}
        
        for k in range(len(tiledata['tilepath'])):
            children.append(html.Div([html.Img(src=tiledata['tilepath'][k], id=tiledata['tileid'][k])]))
        for k in range(len(textdata['text'])):
            children.append(html.Div([html.H4(textdata['text'][k], id=textdata['textid'][k])]))
        children.append(html.Div([html.Img(src=playerdata['playerpath'][0], id=playerdata['playerid'][0])]))
        
        sty_img = {'display': 'block'}
        sty_select = {'display': 'block'}
        sty_enter = {'display': 'block'}
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Up','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_up','text_down','text_enter']}
            sty_img = {'display': 'none'}
        elif button_state['LOCK'] == 3:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        elif button_state['LOCK'] == 0:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Save','Load','Up','Left','Right','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield',
                      'text_save','text_load','text_up','text_left','text_right','text_down','text_enter']}
        elif button_state['LOCK'] == 4:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
            sty_enter = {'display': 'none'}
        elif button_state['LOCK'] == 5:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        for k in range(len(textdata_template['text'])):
            children.append(html.Div([html.H4(textdata_template['text'][k], id=textdata_template['textid'][k])]))
        
        button_state.update({'HPDOUBLE': n_cli_hpd})
        sty_start = {'display': 'none'}
        sty_book = {'display': 'block'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
        if player_dict['TOOL'][1] == '1':
            sty_pick = {'display': 'block'}
        if player_dict['TOOL'][2] == '1':
            sty_tel = {'display': 'block'}
        if player_dict['TOOL'][4] == '1':
            sty_poi = {'display': 'block'}
        if player_dict['TOOL'][5] == '1':
            sty_hpd = {'display': 'block'}
        if player_dict['TOOL'][6] == '1':
            sty_god = {'display': 'block'}
    
    elif n_cli_pick > button_state['PICKAXE']:
        children = template()
        playerid = 'tile{}'.format(player_dict['POS'])
        playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
        
        if button_state['LOCK'] == 0:
            pos_new = player_dict['POS'] + 1
            player_pos_new = 'tile{}'.format(pos_new)
            tiledata = floor_map(player_dict['POSF'])
            if player_pos_new in list(tiledata.values())[1]:
                path_query = list(tiledata.values())[0][list(tiledata.values())[1].index(player_pos_new)]
                playerid = 'tile{}'.format(player_dict['POS'])
                if path_query[-7:-4] == 't11':
                    tool_list = list(player_dict['TOOL'])
                    tool_list[1] = '0'
                    player_dict.update({'WBREAK': pos_new, 'TOOL': ''.join(tool_list)})
        
        if button_state['LOCK'] == 1:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection1'))
        elif button_state['LOCK'] == 2:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection2'))
        elif button_state['LOCK'] == 3 or button_state['LOCK'] == 4:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
        elif button_state['LOCK'] == 5:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div(id='selection1'))
        
        tiledata = floor_map(player_dict['POSF'])
        if player_dict['POI'] == 1:
            status = 'Poison'
        else:
            status = 'Normal'
        textdata = {'text':['{}F'.format(player_dict['POSF']),status,player_dict['LVL'],player_dict['HP'],player_dict['ATK'],player_dict['DEN'],
                            player_dict['GHOLD'],player_dict['XPHOLD'],player_dict['YKEY'],player_dict['BKEY'],player_dict['RKEY']],
                    'textid':['var_floor','var_status','var_lvl','var_hp','var_atk','var_den','var_ghold','var_xphold','var_ykey','var_bkey','var_rkey']}
        
        for k in range(len(tiledata['tilepath'])):
            children.append(html.Div([html.Img(src=tiledata['tilepath'][k], id=tiledata['tileid'][k])]))
        for k in range(len(textdata['text'])):
            children.append(html.Div([html.H4(textdata['text'][k], id=textdata['textid'][k])]))
        children.append(html.Div([html.Img(src=playerdata['playerpath'][0], id=playerdata['playerid'][0])]))
        
        sty_img = {'display': 'block'}
        sty_select = {'display': 'block'}
        sty_enter = {'display': 'block'}
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Up','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_up','text_down','text_enter']}
            sty_img = {'display': 'none'}
        elif button_state['LOCK'] == 3:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        elif button_state['LOCK'] == 0:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Save','Load','Up','Left','Right','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield',
                      'text_save','text_load','text_up','text_left','text_right','text_down','text_enter']}
        elif button_state['LOCK'] == 4:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
            sty_enter = {'display': 'none'}
        elif button_state['LOCK'] == 5:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        for k in range(len(textdata_template['text'])):
            children.append(html.Div([html.H4(textdata_template['text'][k], id=textdata_template['textid'][k])]))
        if player_dict['TOOL'][7] == '1':
            if player_dict['TOOL'][9] == '1':
                children.append(html.Div([html.Img(src='../static/i22.png', id='tool_sword')]))
            else:
                children.append(html.Div([html.Img(src='../static/i21.png', id='tool_sword')]))
        if player_dict['TOOL'][8] == '1':
            if player_dict['TOOL'][10] == '1':
                children.append(html.Div([html.Img(src='../static/i24.png', id='tool_shield')]))
            else:
                children.append(html.Div([html.Img(src='../static/i23.png', id='tool_shield')]))
        
        button_state.update({'PICKAXE': n_cli_pick})
        sty_start = {'display': 'none'}
        sty_book = {'display': 'block'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
        if player_dict['TOOL'][1] == '1':
            sty_pick = {'display': 'block'}
        if player_dict['TOOL'][2] == '1':
            sty_tel = {'display': 'block'}
        if player_dict['TOOL'][4] == '1':
            sty_poi = {'display': 'block'}
        if player_dict['TOOL'][5] == '1':
            sty_hpd = {'display': 'block'}
        if player_dict['TOOL'][6] == '1':
            sty_god = {'display': 'block'}
    
    elif n_cli_tel > button_state['TELEPORT']:
        children = template()
        playerid = 'tile{}'.format(player_dict['POS'])
        playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
        
        if button_state['LOCK'] == 0:
            x_transform_table = {'06':'17','07':'16','08':'15','09':'14','10':'13','11':'12','12':'11','13':'10','14':'09','15':'08','16':'07','17':'06'}
            y_transform_table = {'02':'13','03':'12','04':'11','05':'10','06':'09','07':'08','08':'07','09':'06','10':'05','11':'04','12':'03','13':'02'}
            x = str(player_dict['POS'])[1:3]
            y = str(player_dict['POS'])[3:5]
            x_transform = x_transform_table[x]
            y_transform = y_transform_table[y]
            pos_new = '2{}{}'.format(x_transform,y_transform)
            player_pos_new = 'tile{}'.format(pos_new)
            tiledata = floor_map(player_dict['POSF'])
            if player_pos_new not in list(tiledata.values())[1]:
                tile_pos_new = 'tile{}'.format(int(pos_new) - 10000)
                path_query = list(tiledata.values())[0][list(tiledata.values())[1].index(tile_pos_new)]
                if path_query[-6:-4] == '01' or path_query[-6:-4] == '02':
                    tool_list = list(player_dict['TOOL'])
                    tool_list[2] = '0'
                    player_dict.update({'POS': int(pos_new), 'TOOL': ''.join(tool_list)})
                    playerdata = {'playerpath':['../static/c01.png'], 'playerid':[player_pos_new]}
        
        if button_state['LOCK'] == 1:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection1'))
        elif button_state['LOCK'] == 2:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection2'))
        elif button_state['LOCK'] == 3 or button_state['LOCK'] == 4:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
        elif button_state['LOCK'] == 5:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div(id='selection1'))
        
        tiledata = floor_map(player_dict['POSF'])
        if player_dict['POI'] == 1:
            status = 'Poison'
        else:
            status = 'Normal'
        textdata = {'text':['{}F'.format(player_dict['POSF']),status,player_dict['LVL'],player_dict['HP'],player_dict['ATK'],player_dict['DEN'],
                            player_dict['GHOLD'],player_dict['XPHOLD'],player_dict['YKEY'],player_dict['BKEY'],player_dict['RKEY']],
                    'textid':['var_floor','var_status','var_lvl','var_hp','var_atk','var_den','var_ghold','var_xphold','var_ykey','var_bkey','var_rkey']}
        
        for k in range(len(tiledata['tilepath'])):
            children.append(html.Div([html.Img(src=tiledata['tilepath'][k], id=tiledata['tileid'][k])]))
        for k in range(len(textdata['text'])):
            children.append(html.Div([html.H4(textdata['text'][k], id=textdata['textid'][k])]))
        children.append(html.Div([html.Img(src=playerdata['playerpath'][0], id=playerdata['playerid'][0])]))
        
        sty_img = {'display': 'block'}
        sty_select = {'display': 'block'}
        sty_enter = {'display': 'block'}
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Up','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_up','text_down','text_enter']}
            sty_img = {'display': 'none'}
        elif button_state['LOCK'] == 3:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        elif button_state['LOCK'] == 0:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Save','Load','Up','Left','Right','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield',
                      'text_save','text_load','text_up','text_left','text_right','text_down','text_enter']}
        elif button_state['LOCK'] == 4:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
            sty_enter = {'display': 'none'}
        elif button_state['LOCK'] == 5:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        for k in range(len(textdata_template['text'])):
            children.append(html.Div([html.H4(textdata_template['text'][k], id=textdata_template['textid'][k])]))
        
        button_state.update({'TELEPORT': n_cli_tel})
        sty_start = {'display': 'none'}
        sty_book = {'display': 'block'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
        if player_dict['TOOL'][1] == '1':
            sty_pick = {'display': 'block'}
        if player_dict['TOOL'][2] == '1':
            sty_tel = {'display': 'block'}
        if player_dict['TOOL'][4] == '1':
            sty_poi = {'display': 'block'}
        if player_dict['TOOL'][5] == '1':
            sty_hpd = {'display': 'block'}
        if player_dict['TOOL'][6] == '1':
            sty_god = {'display': 'block'}
    
    elif n_cli_book > button_state['BOOK']:
        children = template()
        playerid = 'tile{}'.format(player_dict['POS'])
        playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
        
        tiledata = floor_map(player_dict['POSF'])
        
        if button_state['LOCK'] == 3:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
        
        elif button_state['LOCK'] == 0:
            monster_list = []
            for i in range(len(list(tiledata.values())[0])):
                if list(tiledata.values())[0][i][-7:-6] == 'c':
                    if list(tiledata.values())[0][i][-6:-5] != '7':
                        if list(tiledata.values())[0][i][-7:-4] not in monster_list:
                            monster_list.append(list(tiledata.values())[0][i][-7:-4])
            
            for i in range(len(monster_list)):
                monster_query = list(monster_dict.values())[7].index(monster_list[i])
                name = list(monster_dict.values())[0][monster_query]
                hp = list(monster_dict.values())[1][monster_query]
                atk = list(monster_dict.values())[2][monster_query]
                den = list(monster_dict.values())[3][monster_query]
                skill = list(monster_dict.values())[4][monster_query]
                skill_text = ''
                if skill == 2:
                    skill_text = 'Attack 2 times'
                elif skill == 3:
                    skill_text = 'Poisonous'
                if player_dict['TOOL'][6] == '1':
                    gdrop = list(monster_dict.values())[5][monster_query] * 2
                else:
                    gdrop = list(monster_dict.values())[5][monster_query]
                xpdrop = list(monster_dict.values())[6][monster_query]
                
                children.append(html.Div([html.Img(src='../static/{}.png'.format(monster_list[i]), id='book{}_icon'.format((i+1)*2-1))]))
                children.append(html.Div([html.H4('{}  HP{}  ATK{}  DEF{}'.format(name,hp,atk,den), id='book{}_text'.format((i+1)*2-1))]))
                children.append(html.Div([html.H4('Gold {}  EXP{}  {}'.format(gdrop,xpdrop,skill_text), id='book{}_text'.format((i+1)*2))]))
            children.append(html.Div(id='book'))
            button_state.update({'LOCK':3})
        
        if button_state['LOCK'] == 1:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection1'))
        elif button_state['LOCK'] == 2:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection2'))
        elif button_state['LOCK'] == 4:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
        elif button_state['LOCK'] == 5:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div(id='selection1'))
        
        if player_dict['POI'] == 1:
            status = 'Poison'
        else:
            status = 'Normal'
        textdata = {'text':['{}F'.format(player_dict['POSF']),status,player_dict['LVL'],player_dict['HP'],player_dict['ATK'],player_dict['DEN'],
                            player_dict['GHOLD'],player_dict['XPHOLD'],player_dict['YKEY'],player_dict['BKEY'],player_dict['RKEY']],
                    'textid':['var_floor','var_status','var_lvl','var_hp','var_atk','var_den','var_ghold','var_xphold','var_ykey','var_bkey','var_rkey']}
        
        for k in range(len(tiledata['tilepath'])):
            children.append(html.Div([html.Img(src=tiledata['tilepath'][k], id=tiledata['tileid'][k])]))
        for k in range(len(textdata['text'])):
            children.append(html.Div([html.H4(textdata['text'][k], id=textdata['textid'][k])]))
        children.append(html.Div([html.Img(src=playerdata['playerpath'][0], id=playerdata['playerid'][0])]))
        
        sty_img = {'display': 'block'}
        sty_select = {'display': 'block'}
        sty_enter = {'display': 'block'}
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Up','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_up','text_down','text_enter']}
            sty_img = {'display': 'none'}
        elif button_state['LOCK'] == 3:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        elif button_state['LOCK'] == 0:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Save','Load','Up','Left','Right','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield',
                      'text_save','text_load','text_up','text_left','text_right','text_down','text_enter']}
        elif button_state['LOCK'] == 4:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
            sty_enter = {'display': 'none'}
        elif button_state['LOCK'] == 5:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        for k in range(len(textdata_template['text'])):
            children.append(html.Div([html.H4(textdata_template['text'][k], id=textdata_template['textid'][k])]))
        if player_dict['TOOL'][7] == '1':
            if player_dict['TOOL'][9] == '1':
                children.append(html.Div([html.Img(src='../static/i22.png', id='tool_sword')]))
            else:
                children.append(html.Div([html.Img(src='../static/i21.png', id='tool_sword')]))
        if player_dict['TOOL'][8] == '1':
            if player_dict['TOOL'][10] == '1':
                children.append(html.Div([html.Img(src='../static/i24.png', id='tool_shield')]))
            else:
                children.append(html.Div([html.Img(src='../static/i23.png', id='tool_shield')]))
        
        button_state.update({'BOOK': n_cli_book})
        sty_start = {'display': 'none'}
        sty_book = {'display': 'block'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
        if player_dict['TOOL'][1] == '1':
            sty_pick = {'display': 'block'}
        if player_dict['TOOL'][2] == '1':
            sty_tel = {'display': 'block'}
        if player_dict['TOOL'][4] == '1':
            sty_poi = {'display': 'block'}
        if player_dict['TOOL'][5] == '1':
            sty_hpd = {'display': 'block'}
        if player_dict['TOOL'][6] == '1':
            sty_god = {'display': 'block'}
    
    elif n_cli_save > button_state['SAVE']:
        children = template()
        playerid = 'tile{}'.format(player_dict['POS'])
        playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
        
        if button_state['LOCK'] == 0:
            talk.update({'conversation': 'You can save the status',
                                     'selection1': 'Save (Click Okay)', 'selection2': 'Not Save (Click Okay)'})
            button_state.update({'LOCK':1, 'SELECT': 4})
        
        if button_state['LOCK'] == 1:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection1'))
        elif button_state['LOCK'] == 2:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection2'))
        elif button_state['LOCK'] == 3 or button_state['LOCK'] == 4:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
        elif button_state['LOCK'] == 5:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div(id='selection1'))
        
        tiledata = floor_map(player_dict['POSF'])
        if player_dict['POI'] == 1:
            status = 'Poison'
        else:
            status = 'Normal'
        textdata = {'text':['{}F'.format(player_dict['POSF']),status,player_dict['LVL'],player_dict['HP'],player_dict['ATK'],player_dict['DEN'],
                            player_dict['GHOLD'],player_dict['XPHOLD'],player_dict['YKEY'],player_dict['BKEY'],player_dict['RKEY']],
                    'textid':['var_floor','var_status','var_lvl','var_hp','var_atk','var_den','var_ghold','var_xphold','var_ykey','var_bkey','var_rkey']}
        
        for k in range(len(tiledata['tilepath'])):
            children.append(html.Div([html.Img(src=tiledata['tilepath'][k], id=tiledata['tileid'][k])]))
        for k in range(len(textdata['text'])):
            children.append(html.Div([html.H4(textdata['text'][k], id=textdata['textid'][k])]))
        children.append(html.Div([html.Img(src=playerdata['playerpath'][0], id=playerdata['playerid'][0])]))
        
        sty_img = {'display': 'block'}
        sty_select = {'display': 'block'}
        sty_enter = {'display': 'block'}
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Up','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_up','text_down','text_enter']}
            sty_img = {'display': 'none'}
        elif button_state['LOCK'] == 3:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        elif button_state['LOCK'] == 0:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Save','Load','Up','Left','Right','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield',
                      'text_save','text_load','text_up','text_left','text_right','text_down','text_enter']}
        elif button_state['LOCK'] == 4:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
            sty_enter = {'display': 'none'}
        elif button_state['LOCK'] == 5:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        for k in range(len(textdata_template['text'])):
            children.append(html.Div([html.H4(textdata_template['text'][k], id=textdata_template['textid'][k])]))
        if player_dict['TOOL'][7] == '1':
            if player_dict['TOOL'][9] == '1':
                children.append(html.Div([html.Img(src='../static/i22.png', id='tool_sword')]))
            else:
                children.append(html.Div([html.Img(src='../static/i21.png', id='tool_sword')]))
        if player_dict['TOOL'][8] == '1':
            if player_dict['TOOL'][10] == '1':
                children.append(html.Div([html.Img(src='../static/i24.png', id='tool_shield')]))
            else:
                children.append(html.Div([html.Img(src='../static/i23.png', id='tool_shield')]))
        
        button_state.update({'SAVE': n_cli_save})
        sty_start = {'display': 'none'}
        sty_book = {'display': 'block'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
        if player_dict['TOOL'][1] == '1':
            sty_pick = {'display': 'block'}
        if player_dict['TOOL'][2] == '1':
            sty_tel = {'display': 'block'}
        if player_dict['TOOL'][4] == '1':
            sty_poi = {'display': 'block'}
        if player_dict['TOOL'][5] == '1':
            sty_hpd = {'display': 'block'}
        if player_dict['TOOL'][6] == '1':
            sty_god = {'display': 'block'}
    
    elif n_cli_load > button_state['LOAD']:
        children = template()
        playerid = 'tile{}'.format(player_dict['POS'])
        playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
        
        if button_state['LOCK'] == 0:
            talk.update({'conversation': 'You can load the status',
                                     'selection1': 'Load (Click Okay)', 'selection2': 'Not Load (Click Okay)'})
            button_state.update({'LOCK':1, 'SELECT': 5})
        
        if button_state['LOCK'] == 1:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection1'))
        elif button_state['LOCK'] == 2:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div([html.H4(talk['selection2'], id='text_selection2')]))
            children.append(html.Div(id='selection2'))
        elif button_state['LOCK'] == 3 or button_state['LOCK'] == 4:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
        elif button_state['LOCK'] == 5:
            children.append(html.Div(id='conversation'))
            children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
            children.append(html.Div([html.H4(talk['selection1'], id='text_selection1')]))
            children.append(html.Div(id='selection1'))
        
        tiledata = floor_map(player_dict['POSF'])
        if player_dict['POI'] == 1:
            status = 'Poison'
        else:
            status = 'Normal'
        textdata = {'text':['{}F'.format(player_dict['POSF']),status,player_dict['LVL'],player_dict['HP'],player_dict['ATK'],player_dict['DEN'],
                            player_dict['GHOLD'],player_dict['XPHOLD'],player_dict['YKEY'],player_dict['BKEY'],player_dict['RKEY']],
                    'textid':['var_floor','var_status','var_lvl','var_hp','var_atk','var_den','var_ghold','var_xphold','var_ykey','var_bkey','var_rkey']}
        
        for k in range(len(tiledata['tilepath'])):
            children.append(html.Div([html.Img(src=tiledata['tilepath'][k], id=tiledata['tileid'][k])]))
        for k in range(len(textdata['text'])):
            children.append(html.Div([html.H4(textdata['text'][k], id=textdata['textid'][k])]))
        children.append(html.Div([html.Img(src=playerdata['playerpath'][0], id=playerdata['playerid'][0])]))
        
        sty_img = {'display': 'block'}
        sty_select = {'display': 'block'}
        sty_enter = {'display': 'block'}
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Up','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_up','text_down','text_enter']}
            sty_img = {'display': 'none'}
        elif button_state['LOCK'] == 3:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        elif button_state['LOCK'] == 0:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Save','Load','Up','Left','Right','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield',
                      'text_save','text_load','text_up','text_left','text_right','text_down','text_enter']}
        elif button_state['LOCK'] == 4:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
            sty_enter = {'display': 'none'}
        elif button_state['LOCK'] == 5:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        for k in range(len(textdata_template['text'])):
            children.append(html.Div([html.H4(textdata_template['text'][k], id=textdata_template['textid'][k])]))
        if player_dict['TOOL'][7] == '1':
            if player_dict['TOOL'][9] == '1':
                children.append(html.Div([html.Img(src='../static/i22.png', id='tool_sword')]))
            else:
                children.append(html.Div([html.Img(src='../static/i21.png', id='tool_sword')]))
        if player_dict['TOOL'][8] == '1':
            if player_dict['TOOL'][10] == '1':
                children.append(html.Div([html.Img(src='../static/i24.png', id='tool_shield')]))
            else:
                children.append(html.Div([html.Img(src='../static/i23.png', id='tool_shield')]))
        
        button_state.update({'LOAD': n_cli_load})
        sty_start = {'display': 'none'}
        sty_book = {'display': 'block'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
        if player_dict['TOOL'][1] == '1':
            sty_pick = {'display': 'block'}
        if player_dict['TOOL'][2] == '1':
            sty_tel = {'display': 'block'}
        if player_dict['TOOL'][4] == '1':
            sty_poi = {'display': 'block'}
        if player_dict['TOOL'][5] == '1':
            sty_hpd = {'display': 'block'}
        if player_dict['TOOL'][6] == '1':
            sty_god = {'display': 'block'}
    
    elif n_cli_enter > button_state['ENTER']:
        children = template()
        
        if button_state['LOCK'] == 3: #all handling finished, enter to clear conversation box
            button_state.update({'LOCK':0})
        
        elif button_state['LOCK'] == 1:
            talk.update({'selection1': '', 'selection2': ''})
            if button_state['SELECT'] == 1:
                event_list = list(player_dict['EVENT'])
                if event_list[1] == '0':
                    if player_dict['GHOLD'] >= 50:
                        event_list[0] = '1'
                        talk.update({'conversation': ''})
                        player_dict.update({'EVENT': ''.join(event_list), 'GHOLD': player_dict['GHOLD'] - 50, 'BKEY': player_dict['BKEY'] + 1})
                        button_state.update({'LOCK':0})
                    else:
                        talk.update({'conversation': 'Not enough GOLD (Click Okay)'})
                        children.append(html.Div(id='conversation'))
                        children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
                        button_state.update({'LOCK':3})
                else:
                    talk.update({'conversation': 'You cannot buy again (Click Okay)'})
                    children.append(html.Div(id='conversation'))
                    children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
                    button_state.update({'LOCK':3})
            elif button_state['SELECT'] == 2:
                if player_dict['GHOLD'] >= player_dict['GOLDUP'] * 20:
                    talk.update({'conversation': ''})
                    player_dict.update({'GHOLD': player_dict['GHOLD'] - player_dict['GOLDUP'] * 20,
                                        'ATK': player_dict['ATK'] + 3, 'DEN': player_dict['DEN'] + 3, 'GOLDUP': player_dict['GOLDUP'] + 1})
                    button_state.update({'LOCK':0})
                else:
                    talk.update({'conversation': 'Not enough GOLD (Click Okay)'})
                    children.append(html.Div(id='conversation'))
                    children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
                    button_state.update({'LOCK':3})
            elif button_state['SELECT'] == 3:
                if player_dict['XPHOLD'] >= player_dict['XPUP'] * 40:
                    talk.update({'conversation': ''})
                    player_dict.update({'XPHOLD': player_dict['XPHOLD'] - player_dict['XPUP'] * 40, 'LVL': player_dict['LVL'] + 1,
                                        'ATK': player_dict['ATK'] + 5, 'DEN': player_dict['DEN'] + 5, 'XPUP': player_dict['XPUP'] + 1})
                    button_state.update({'LOCK':0})
                else:
                    talk.update({'conversation': 'Not enough EXP (Click Okay)'})
                    children.append(html.Div(id='conversation'))
                    children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
                    button_state.update({'LOCK':3})
            elif button_state['SELECT'] == 4:
                player_dict_save.update(player_dict)
                talk.update({'conversation': ''})
                button_state.update({'LOCK':0})
            elif button_state['SELECT'] == 5:
                if len(player_dict_save) > 0:
                    player_dict.update(player_dict_save)
                    talk.update({'conversation': ''})
                    button_state.update({'LOCK':0})
                else:
                    talk.update({'conversation': 'You do not have any save (Click Okay)'})
                    children.append(html.Div(id='conversation'))
                    children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
                    button_state.update({'LOCK':4})
        
        elif button_state['LOCK'] == 2:
            talk.update({'conversation': '', 'selection1': '', 'selection2': ''})
            button_state.update({'LOCK':0})
        elif button_state['LOCK'] == 3:
            talk.update({'conversation': ''})
        elif button_state['LOCK'] == 5:
            if len(player_dict_save) > 0:
                player_dict.update(player_dict_save)
                talk.update({'conversation': ''})
                button_state.update({'LOCK':0})
            else:
                talk.update({'conversation': 'You do not have any save (Click Okay)'})
                children.append(html.Div(id='conversation'))
                children.append(html.Div([html.H4(talk['conversation'], id='text_conversation')]))
                button_state.update({'LOCK':3})
        
        playerid = 'tile{}'.format(player_dict['POS'])
        playerdata = {'playerpath':['../static/c01.png'], 'playerid':[playerid]}
        
        tiledata = floor_map(player_dict['POSF'])
        if player_dict['POI'] == 1:
            status = 'Poison'
        else:
            status = 'Normal'
        textdata = {'text':['{}F'.format(player_dict['POSF']),status,player_dict['LVL'],player_dict['HP'],player_dict['ATK'],player_dict['DEN'],
                            player_dict['GHOLD'],player_dict['XPHOLD'],player_dict['YKEY'],player_dict['BKEY'],player_dict['RKEY']],
                    'textid':['var_floor','var_status','var_lvl','var_hp','var_atk','var_den','var_ghold','var_xphold','var_ykey','var_bkey','var_rkey']}
        
        for k in range(len(tiledata['tilepath'])):
            children.append(html.Div([html.Img(src=tiledata['tilepath'][k], id=tiledata['tileid'][k])]))
        for k in range(len(textdata['text'])):
            children.append(html.Div([html.H4(textdata['text'][k], id=textdata['textid'][k])]))
        children.append(html.Div([html.Img(src=playerdata['playerpath'][0], id=playerdata['playerid'][0])]))
        
        sty_img = {'display': 'block'}
        sty_select = {'display': 'block'}
        sty_enter = {'display': 'block'}
        if button_state['LOCK'] == 1 or button_state['LOCK'] == 2:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Up','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_up','text_down','text_enter']}
            sty_img = {'display': 'none'}
        elif button_state['LOCK'] == 3:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield','text_enter']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
        elif button_state['LOCK'] == 0:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD','Save','Load','Up','Left','Right','Down','Okay'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield',
                      'text_save','text_load','text_up','text_left','text_right','text_down','text_enter']}
        elif button_state['LOCK'] == 4:
            textdata_template = {
                'text':['LVL','HP','ATK','DEF','GOLD','EXP','SWORD','SHIELD'],
                'textid':['text_lvl','text_hp','text_atk','text_den','text_ghold','text_xphold','text_sword','text_shield']}
            sty_img = {'display': 'none'}
            sty_select = {'display': 'none'}
            sty_enter = {'display': 'none'}
        for k in range(len(textdata_template['text'])):
            children.append(html.Div([html.H4(textdata_template['text'][k], id=textdata_template['textid'][k])]))
        if player_dict['TOOL'][7] == '1':
            if player_dict['TOOL'][9] == '1':
                children.append(html.Div([html.Img(src='../static/i22.png', id='tool_sword')]))
            else:
                children.append(html.Div([html.Img(src='../static/i21.png', id='tool_sword')]))
        if player_dict['TOOL'][8] == '1':
            if player_dict['TOOL'][10] == '1':
                children.append(html.Div([html.Img(src='../static/i24.png', id='tool_shield')]))
            else:
                children.append(html.Div([html.Img(src='../static/i23.png', id='tool_shield')]))
        
        button_state.update({'ENTER': n_cli_enter})
        sty_start = {'display': 'none'}
        sty_book = {'display': 'block'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
        if player_dict['TOOL'][1] == '1':
            sty_pick = {'display': 'block'}
        if player_dict['TOOL'][2] == '1':
            sty_tel = {'display': 'block'}
        if player_dict['TOOL'][4] == '1':
            sty_poi = {'display': 'block'}
        if player_dict['TOOL'][5] == '1':
            sty_hpd = {'display': 'block'}
        if player_dict['TOOL'][6] == '1':
            sty_god = {'display': 'block'}
    
    else:
        children = html.Div([html.H4('Click Start to Start the game', id='text_start')])
        button_state.update({'START': 0})
        sty_start = {'display': 'block'}
        sty_img = {'display': 'none'}
        sty_select = {'display': 'none'}
        sty_enter = {'display': 'none'}
        sty_book = {'display': 'none'}
        sty_pick = {'display': 'none'}
        sty_tel = {'display': 'none'}
        sty_poi = {'display': 'none'}
        sty_hpd = {'display': 'none'}
        sty_god = {'display': 'none'}
    
    return children,sty_start,sty_img,sty_img,sty_select,sty_img,sty_select,sty_img,sty_enter,sty_book,sty_pick,sty_tel,sty_poi,sty_hpd,sty_god