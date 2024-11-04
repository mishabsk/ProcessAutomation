import xml.etree.ElementTree as ET
import zipfile

uploaded_file = r'C:\Users\abhasker1\Downloads\EmilyTeohProject\File2.docx'

with zipfile.ZipFile(uploaded_file, 'r') as docx:
    with docx.open('word/document.xml') as xml_file:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        namespaces = {
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
        }

    # Initialize dictionaries to store bookmark names and references
    bookmark_names = {}
    referenced_bookmarks = []

    # Extract bookmark names and ids
    for bookmark_start in root.findall('.//w:bookmarkStart', namespaces):
        bookmark_name = bookmark_start.attrib.get(f'{{{namespaces["w"]}}}name')
        bookmark_id = bookmark_start.attrib.get(f'{{{namespaces["w"]}}}id')
        if bookmark_id and bookmark_name:
            bookmark_names[bookmark_id] = bookmark_name

    # Check for references to bookmarks in hyperlinks
    for hyperlink in root.findall('.//w:hyperlink', namespaces):
        # Check the bookmark referenced by the hyperlink
        for child in hyperlink:
            if child.tag.endswith('anchor'):  # 'anchor' is used in Word to reference a bookmark by name
                bookmark_name = child.attrib.get(f'{{{namespaces["w"]}}}anchor')
                if bookmark_name in bookmark_names.values():
                    referenced_bookmarks.append(bookmark_name)

    # Determine unreferenced bookmarks
    unreferenced_bookmarks = [name for name in bookmark_names.values() if name not in referenced_bookmarks]
    
    # Output results
    if unreferenced_bookmarks:
        print("Unreferenced bookmarks:")
        for bookmark in unreferenced_bookmarks:
            print(f"- {bookmark}")
    else:
        print("All bookmarks are correctly referenced.")
