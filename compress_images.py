#!/usr/bin/env python3
"""
Image Compression Script
Converts .webp images to compressed .png files for better web compatibility
"""

import os
import glob
from PIL import Image
import sys

def compress_images():
    """Convert .webp images to compressed .png files"""
    
    # Check if Pillow is installed
    try:
        from PIL import Image
    except ImportError:
        print("❌ Pillow not installed. Please run: pip install Pillow")
        return False
    
    # Source and destination directories
    source_dir = "public/images"
    dest_dir = "public/images_compressed"
    
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"📁 Created directory: {dest_dir}")
    
    # Find all .webp files
    webp_files = glob.glob(os.path.join(source_dir, "*.webp"))
    
    if not webp_files:
        print("❌ No .webp files found in public/images/")
        return False
    
    print(f"🖼️ Found {len(webp_files)} .webp files to convert")
    
    converted_count = 0
    total_original_size = 0
    total_compressed_size = 0
    
    for webp_file in webp_files:
        try:
            # Get filename without extension
            filename = os.path.basename(webp_file)
            name_without_ext = os.path.splitext(filename)[0]
            png_file = os.path.join(dest_dir, f"{name_without_ext}.png")
            
            # Open and convert image
            with Image.open(webp_file) as img:
                # Convert to RGB if necessary (PNG doesn't support RGBA for web)
                if img.mode in ('RGBA', 'LA'):
                    # Create white background
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'RGBA':
                        background.paste(img, mask=img.split()[-1])  # Use alpha channel as mask
                    else:
                        background.paste(img)
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize if too large (max 512x512 for web)
                if img.size[0] > 512 or img.size[1] > 512:
                    img.thumbnail((512, 512), Image.Resampling.LANCZOS)
                
                # Save as compressed PNG
                img.save(png_file, 'PNG', optimize=True, quality=85)
            
            # Calculate size savings
            original_size = os.path.getsize(webp_file)
            compressed_size = os.path.getsize(png_file)
            
            total_original_size += original_size
            total_compressed_size += compressed_size
            
            # Calculate compression ratio
            compression_ratio = (1 - compressed_size / original_size) * 100
            
            print(f"✅ {filename} -> {name_without_ext}.png ({compression_ratio:.1f}% smaller)")
            print(f"   Original: {original_size/1024:.1f}KB -> Compressed: {compressed_size/1024:.1f}KB")
            
            converted_count += 1
            
        except Exception as e:
            print(f"❌ Error converting {webp_file}: {e}")
    
    # Summary
    print(f"\n🎉 Conversion complete!")
    print(f"📊 Converted: {converted_count}/{len(webp_files)} files")
    print(f"💾 Total size reduction: {(1 - total_compressed_size / total_original_size) * 100:.1f}%")
    print(f"📁 Compressed images saved to: {dest_dir}/")
    
    return True

if __name__ == "__main__":
    print("🖼️ Image Compression Tool")
    print("Converting .webp files to compressed .png files...")
    print()
    
    success = compress_images()
    
    if success:
        print("\n✅ Ready to update the game code to use compressed PNG files!")
        print("📝 Next steps:")
        print("1. Update processImageUrl() to use .png extension")
        print("2. Update image paths to use images_compressed/ folder")
        print("3. Commit and push the changes")
    else:
        print("\n❌ Compression failed. Please check the errors above.")
