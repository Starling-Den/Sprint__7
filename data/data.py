from data import generators


class DataCourierRegLogin:
    data_successful = [
        {
            'login': generators.login_generator(),
            'password': generators.password_generator(),
            'firstName': generators.name_generator(),
        }
    ]
    data_deficit_reg = [
        {
            'password': generators.password_generator(),
            'firstName': generators.name_generator(),
        },
        {
            'login': generators.login_generator(),
            'firstName': generators.name_generator(),
        },

    ]
    data_login = [
        {
            'login': generators.login_generator(),
            'password': generators.password_generator(),
        }
    ]

class ResponseBodyCourier:
    courier_login_without_login_or_password = {'code': 400, 'message': 'Недостаточно данных для входа'}
    courier_login_not_exist = {'code': 404, 'message': 'Учетная запись не найдена'}
    courier_registration = {'ok': True}
    courier_registration_without_login_or_password = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    courier_registration_with_exist_login = {'code': 409, 'message': 'Этот логин уже используется'}

class DataCreateOrder:
    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+79823553535",
        "rentTime": 5,
        "deliveryDate": "2025-07-30",
        "comment": "Saske, come back to Konoha",
    }
    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]


create_order_true = 'track'
get_list_order_true = 'orders'
