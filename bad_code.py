#!/usr/local/bin/python3

import csv
import logging
import os

import mock_service

REJECT_DEST_EMAIL = "feed@marketdial.com"

def send_report(db_client, rejects=False):
    if rejects:
        file_name = "TC_Reject_Report.csv"
        email = REJECT_DEST_EMAIL
    else:
        file_name = "TC_Finance_Report.csv"
        email = "tc@gmail.com"
        
    items_sold = db_client["client_collection"]["tc_topps"]["items_sold"]
    
    logging.info(f"Starting tc_topps {file_name}")

    for item in items_sold:
        item["name"] = mock_service.SKU_MAP[item["name"]]

    destination_directory = "/tmp/"

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    with open(destination_directory + file_name, "w+") as destination_file:
        writer = csv.DictWriter(destination_file, fieldnames=["name", "price", "quantity_sold"])
        writer.writeheader()
        writer.writerows(items_sold)

    link = mock_service.get_report_link(filename=file_name)

    if rejects:
        sub = "tc_topps rejected properties file."
        cont = f"Here is the rejected properties file link: {link}"
    else:
        sub = "tc_topps report file."
        cont = f"Here is the Report file link: {link}"
    
    try:
        res = mock_service.email_file_link(email, sub, cont)
    except ValueError as value_error:
        logging.error(value_error)
        return False

    logging.info(f"Successfully reported tc_topps {file_name}")
    return res
