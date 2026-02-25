#!/usr/bin/env python
"""
Script to upgrade the database schema for PlaceImage table
"""
from app import app, db
from models import PlaceImage

with app.app_context():
    # Create PlaceImage table if it doesn't exist
    db.create_all()
    print("✅ Database schema updated successfully!")
    print("✅ PlaceImage table created (if it didn't exist)")
