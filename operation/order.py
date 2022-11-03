import requests
from api.order import order
from core.result_base import ResultBase


def pre_submit(cookies):
    """
    请求新建订单页面
    :return: 自定义的关键字返回结果 uuid
    """
    # 下面这种设置cookie是不行的，具体的看rest_client.py源码看取参数的逻辑
    # result = order.pre_submit(cookies=cookies)
    headers = {
        'Cookie': cookies  ## 这里也可以设置cookie
    }
    result = order.pre_submit(headers=headers)
    print("打印cookies开始\n")
    print(cookies)
    print("打印cookies结束\n")
    return result


def batch_match_by_material_no(warehouseLabels, cityId, companyId,
                               materialNoNumberList, strategy, userId, uuid):
    """
    查询型号
    :return: 自定义的关键字返回结果
    """
    payload = {
        "warehouseLabels": warehouseLabels,
        "cityId": cityId,
        "companyId": companyId,
        "materialNoNumberList": materialNoNumberList,
        "strategy": strategy,
        "userId": userId,
        "uuid": uuid
    }
    header = {"Content-Type": "application/json"}
    result = order.batch_match_by_material_no(json=payload, headers=header)
    return ResultBase(result)


def submit_manual_order():
    payload = {
        "uuid":
        "${uuid}",
        "companyId":
        1688,
        "userId":
        1002553,
        "modelDtoList": [{
            "modelId": 529147,
            "shopModelId": 100188962,
            "warehouseId": 633,
            "warehouseLabel": 10,
            "quantity": 1,
            "channelId": 1,
            "scmId": 109652995,
            "modelDescription": "",
            "packSpecification": "",
            "userId": 1002553,
            "brandColor": "#4250d5",
            "sequence": 1,
            "originalPriceYuan": 47.43,
            "salesPriceYuan": 47.43,
            "salesDiscount": 0.3841,
            "goalDiscount": 0.3841,
            "goalPriceYuan": 47.43,
            "promotionPoint": 0,
            "point": 0,
            "averageSalesPriceYuan": 47.43,
            "companyMaterialCode": "H1_H_test_01"
        }],
        "consigneeAddressId":
        35211,
        "provinceId":
        310000,
        "cityId":
        310100,
        "isAgent":
        0,
        "agentAddressId":
        33161,
        "agentFee":
        0,
        "cloudAgent":
        True,
        "transitWarehouseId":
        None,
        "templateId":
        252,
        "expressId":
        1,
        "expressTypeDesc":
        "普通快递",
        "freightFee":
        1000,
        "invoiceType":
        2,
        "invoiceId":
        1354,
        "syncInvoiceAddress":
        False,
        "invoiceAddressId":
        742,
        "contractTemplateId":
        1445,
        "settlementDesc":
        "款到发货",
        "settlementId":
        1,
        "settlementType":
        10,
        "stockOutType":
        10,
        "discountAmountYuan":
        0
    }
    header = {"Content-Type": "application/json"}
    result = order.submit_manual_order(json=payload, headers=header)
    return ResultBase(result)
