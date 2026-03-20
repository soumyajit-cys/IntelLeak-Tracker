from apscheduler.schedulers.background import BackgroundScheduler
from services.scraper import read_local_data
from services.processor import extract_data
from services.matcher import match_keywords
from database import breach_collection

def job():
    raw = read_local_data()
    processed = extract_data(raw)

    breach_collection.insert_one(processed)
    match_keywords(processed)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", minutes=2)
    scheduler.start()