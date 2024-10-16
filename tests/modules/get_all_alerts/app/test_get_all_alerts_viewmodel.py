
# import datetime

# from src.modules.get_similar_notices.app.get_similar_notices_viewmodel import AlertViewmodel, GetAllAlertsViewmodel
# from src.shared.domain.entities.notice_chunk import Alert


# class Test_AlertViewModel:

#     def test_get_all_alert_viewmodel(self):
#         alert = Alert(
#             alert_id="1",
#             type="baixa_carga_bateria",
#             message="A carga da bateria está abaixo de 20%",
#             is_resolved=False,
#             timestamp_created_at=int(datetime.datetime.now().timestamp())*1000,
#             timestamp_updated_at=None
#         )
#         viewmodel = AlertViewmodel(
#             alert=alert).to_dict()

#         expected = {
#             'alert_id': "1",
#             'type': "baixa_carga_bateria",
#             'message': "A carga da bateria está abaixo de 20%",
#             'is_resolved': False,
#             'timestamp_created_at': int(datetime.datetime.now().timestamp())*1000,
#             'timestamp_updated_at': None,
#         }

#         assert expected == viewmodel


# class Test_GetAllAlertsViewModel:

#     def test_get_all_alerts_viewmodel(self):
#         alerts = [
#             Alert(
#                 alert_id="1",
#                 type="baixa_carga_bateria",
#                 message="A carga da bateria está abaixo de 20%",
#                 is_resolved=False,
#                 timestamp_created_at=int(
#                     datetime.datetime.now().timestamp())*1000,
#                 timestamp_updated_at=None
#             ),
#             Alert(
#                 alert_id="2",
#                 type="baixa_carga_bateria",
#                 message="A carga da bateria está abaixo de 20%",
#                 is_resolved=False,
#                 timestamp_created_at=int(
#                     datetime.datetime.now().timestamp())*1000,
#                 timestamp_updated_at=None
#             ),
#             Alert(
#                 alert_id="3",
#                 type="baixa_carga_bateria",
#                 message="A carga da bateria está abaixo de 20%",
#                 is_resolved=False,
#                 timestamp_created_at=int(
#                     datetime.datetime.now().timestamp())*1000,
#                 timestamp_updated_at=None
#             ),
#         ]

#         viewmodel = GetAllAlertsViewmodel(
#             alerts=alerts).to_dict()

#         expected = {
#             'alerts': [
#                 {
#                     'alert_id': "1",
#                     'type': "baixa_carga_bateria",
#                     'message': "A carga da bateria está abaixo de 20%",
#                     'is_resolved': False,
#                     'timestamp_created_at': int(datetime.datetime.now().timestamp())*1000,
#                     'timestamp_updated_at': None,
#                 },
#                 {
#                     'alert_id': "2",
#                     'type': "baixa_carga_bateria",
#                     'message': "A carga da bateria está abaixo de 20%",
#                     'is_resolved': False,
#                     'timestamp_created_at': int(datetime.datetime.now().timestamp())*1000,
#                     'timestamp_updated_at': None,
#                 },
#                 {
#                     'alert_id': "3",
#                     'type': "baixa_carga_bateria",
#                     'message': "A carga da bateria está abaixo de 20%",
#                     'is_resolved': False,
#                     'timestamp_created_at': int(datetime.datetime.now().timestamp())*1000,
#                     'timestamp_updated_at': None,
#                 },
#             ]
#         }

#         assert expected == viewmodel
