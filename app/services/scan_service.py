from app.scraper.scraper import fetch_breach_data
from app.processor.processor import process_data
from app.services.keyword_service import get_keywords
from app.services.breach_service import save_breach_data
from app.services.alert_service import create_alert
from app.alerts.notifier import send_email_alert

def run_scan():
    raw_data = fetch_breach_data()
    processed = process_data(raw_data)

    save_breach_data(processed)

    keywords = get_keywords()

    for item in processed:
        for kw in keywords:
            if kw["value"] in str(item):
                create_alert(kw["value"], item)
                send_email_alert(f"Match found for {kw['value']}: {item}")

    return {"status": "Scan completed"}