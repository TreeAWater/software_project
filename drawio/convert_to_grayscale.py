#!/usr/bin/env python3
"""
Convert all drawio files to grayscale (black and white)
"""
import re
import os
from pathlib import Path

def convert_to_grayscale():
    """Convert all colors in drawio files to grayscale"""
    
    # Define grayscale replacements for fill colors and stroke colors
    # We'll use different shades of gray to maintain visual distinction
    grayscale_fills = {
        '#d5e8d4': '#f0f0f0',  # light green -> light gray
        '#dae8fc': '#e0e0e0',  # light blue -> gray
        '#e1d5e7': '#d0d0d0',  # light purple -> medium light gray
        '#ffe6cc': '#c8c8c8',  # light orange -> medium gray
        '#f8cecc': '#b0b0b0',  # light red -> medium dark gray
        '#fff2cc': '#d8d8d8',  # light yellow -> another gray
        '#f5f5f5': '#f5f5f5',  # already gray, keep it
    }
    
    grayscale_strokes = {
        '#82b366': '#808080',  # green -> gray
        '#6c8ebf': '#606060',  # blue -> dark gray
        '#9673a6': '#707070',  # purple -> medium gray
        '#d79b00': '#505050',  # orange -> darker gray
        '#b85450': '#404040',  # red -> dark gray
        '#d6b656': '#686868',  # yellow -> gray
        '#666666': '#666666',  # already gray, keep it
    }
    
    drawio_dir = Path(__file__).parent
    drawio_files = list(drawio_dir.glob('*.drawio'))
    
    print(f"Found {len(drawio_files)} drawio files to convert:")
    for f in drawio_files:
        print(f"  - {f.name}")
    print()
    
    for drawio_file in drawio_files:
        print(f"Processing: {drawio_file.name}")
        
        with open(drawio_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace fill colors
        for color, gray in grayscale_fills.items():
            content = content.replace(f'fillColor={color}', f'fillColor={gray}')
        
        # Replace stroke colors
        for color, gray in grayscale_strokes.items():
            content = content.replace(f'strokeColor={color}', f'strokeColor={gray}')
        
        # Write back if changed
        if content != original_content:
            with open(drawio_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Converted to grayscale")
        else:
            print(f"  - No color changes needed")
    
    print("\nDone! All drawio files have been converted to grayscale.")

if __name__ == '__main__':
    convert_to_grayscale()
