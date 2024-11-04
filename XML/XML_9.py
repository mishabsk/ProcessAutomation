import xml.etree.ElementTree as ET
import zipfile

def extract_bookmarked_content(root, namespaces):
    bookmark_names = {}
    bookmark_content = {}

    # Extract bookmark names, ids, and collect their content
    for bookmark_start in root.findall('.//w:bookmarkStart', namespaces):
        bookmark_name = bookmark_start.attrib.get(f'{{{namespaces["w"]}}}name')
        bookmark_id = bookmark_start.attrib.get(f'{{{namespaces["w"]}}}id')

        if bookmark_id and bookmark_name:
            bookmark_names[bookmark_id] = bookmark_name

            # Find the corresponding bookmarkEnd using the same ID
            bookmark_end = root.find(f".//w:bookmarkEnd[@w:id='{bookmark_id}']", namespaces)

            if bookmark_end is not None:
                # Collect content between bookmarkStart and bookmarkEnd
                content = []  # List to collect the content between the bookmark start and end
                found_start = False

                # Iterate through all elements and collect text between bookmarkStart and bookmarkEnd
                for elem in root.iter():
                    if elem == bookmark_start:
                        found_start = True
                    elif elem == bookmark_end:
                        break
                    elif found_start:
                        if elem.text:
                            content.append(elem.text.strip())  # Append to the content list

                # Join the content list into a string and store it with the bookmark name
                bookmark_content[bookmark_name] = ' '.join(content)

    return bookmark_names, bookmark_content


# Example usage:
uploaded_file = r'C:\Users\abhasker1\Downloads\EmilyTeohProject\File2.docx'

with zipfile.ZipFile(uploaded_file, 'r') as docx:
    with docx.open('word/document.xml') as xml_file:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        namespaces = {
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
        }

    # Extract bookmarks and their associated content
    bookmark_names, bookmark_content = extract_bookmarked_content(root, namespaces)

    # Output the extracted bookmarks and their content
    for bookmark_id, name in bookmark_names.items():
        print(f"Bookmark: {name}")
        print(f"Content: {bookmark_content.get(name, 'No content found')}")
        print('-' * 40)
