#!/usr/bin/env python3
"""
Capture slides from HTML pitch deck as images
"""
import os
from playwright.sync_api import sync_playwright

HTML_PATH = os.path.join(os.path.dirname(__file__), 'pitch.html')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'slides')

def capture_slides():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        # Load the HTML file
        page.goto(f'file://{os.path.abspath(HTML_PATH)}')
        page.wait_for_timeout(1000)
        
        # Get total slides
        total = page.evaluate('document.querySelectorAll(".s").length')
        print(f"Found {total} slides")
        
        for i in range(total):
            # Navigate to slide
            page.evaluate(f'goTo({i})')
            page.wait_for_timeout(500)  # Wait for animations
            
            # Screenshot
            output_path = os.path.join(OUTPUT_DIR, f'slide_{i+1}.png')
            page.screenshot(path=output_path)
            print(f"✅ Captured slide {i+1}")
        
        browser.close()
    
    print(f"\n📁 Slides saved to: {OUTPUT_DIR}")
    return OUTPUT_DIR

if __name__ == "__main__":
    capture_slides()
