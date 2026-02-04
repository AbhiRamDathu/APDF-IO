import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

print(f"🔍 Testing MongoDB connection...")
print(f"📍 Database: {DATABASE_NAME}")

try:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    db = client[DATABASE_NAME]
    
    # Test ping
    client.admin.command('ping')
    print("✅ MongoDB connection successful!")
    
    # List collections
    collections = db.list_collection_names()
    print(f"✅ Found {len(collections)} collections: {collections}")
    
    # Test write permission
    test_col = db["_connection_test"]
    result = test_col.insert_one({"test": "connection", "timestamp": "2026-02-04"})
    test_col.delete_one({"_id": result.inserted_id})
    print("✅ Write permissions verified!")
    
    print("\n🎉 All database tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n💡 Check:")
    print("  1. MongoDB URI is correct")
    print("  2. IP whitelist includes your current IP (or 0.0.0.0/0)")
    print("  3. Database user has read/write permissions")
