
WEIGHT_EMAIL = 'email'
WEIGHT_IS_ACTIVE = 'is_active'
WEIGHT_USERNAME = 'username'
WEIGHT_AVATAR = 'avatar'
WEIGHT_BIO = 'bio'
WEIGHT_FIRST_NAME = 'first_name'
WEIGHT_LAST_NAME = 'last_name'
WEIGHT_FULL_NAME = 'full_name'

WEIGHT_DISTRIBUTIONS = {
                        WEIGHT_EMAIL: 40,
                        WEIGHT_IS_ACTIVE: 40,
                        WEIGHT_USERNAME: 20,
                        WEIGHT_AVATAR: 30,
                        WEIGHT_BIO: 10,
                        WEIGHT_FULL_NAME: 20,
                    }

# Payment statuses on the TransactionLog model

DBCV_PAYMENT_SERVICE_STATUS_UNPROCESSED = 1
DBCV_PAYMENT_SERVICE_STATUS_PROCESSED = 2
DBCV_PAYMENT_SERVICE_STATUS_ERROR = 3

PAYMENT_STATUSES = (
    (DBCV_PAYMENT_SERVICE_STATUS_UNPROCESSED, 'Unprocessed'),
    (DBCV_PAYMENT_SERVICE_STATUS_PROCESSED, 'Processed'),
    (DBCV_PAYMENT_SERVICE_STATUS_ERROR, 'Error'),
)

# Services types

DBCV_SERVICE_TYPE_AIRTIME = 'AT'
DBCV_SERVICE_TYPE_DATA = 'DB'
DBCV_SERVICE_TYPE_CABLETV = 'CT'
DBCV_SERVICE_TYPE_POWER = 'EL'

SERVICE_TYPES = (
    (DBCV_SERVICE_TYPE_AIRTIME, 'Airtime'),
    (DBCV_SERVICE_TYPE_DATA, 'Data Bundle'),
    (DBCV_SERVICE_TYPE_CABLETV, 'Cable TV'),
    (DBCV_SERVICE_TYPE_POWER, 'Power Bills'),
)
