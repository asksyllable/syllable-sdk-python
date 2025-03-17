import os
import shutil
import json

def get_markdown_files(directory):
    try:
        files = os.listdir(os.path.join('mintlify', directory))
        markdown_files = [
            os.path.join(directory, os.path.splitext(file)[0])
            for file in files if file.endswith('.md')
        ]
        return markdown_files
    except Exception as e:
        print(f"Error reading directory: {e}")
        return []

def move_and_update_files(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_path = os.path.join(root, file)
            if file != 'Overview.mdx' and file.endswith('.md'):
                model = os.path.splitext(file)[0]
                
                if 'docs/sdks/' in src_path and file == 'README.md':
                    type_dir = os.path.basename(os.path.dirname(src_path))
                    dest_path = os.path.join(dest_dir, 'python-sdk-docs', f'{type_dir}.mdx')
                else:
                    dest_path = os.path.join(dest_dir, 'python-sdk-docs', 'models', f'{model}.md')
                
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                with open(src_path, 'r', encoding='utf-8') as f:
                    data = f.read()

                lines = data.split('\n')
                if lines[0].startswith('#'):
                    title = lines[0][1:].strip()
                    lines[0] = f"---\ntitle: '{title}'\n---"

                updated_data = '\n'.join(lines)
                updated_data = updated_data.replace('<!--', '').replace('-->', '')  # Remove HTML comments
                updated_data = updated_data.replace('<Uint8Array>', '')  # Remove HTML conflicts
                updated_data = updated_data.replace('<string, *string*>', '')  # Remove HTML conflicts
                updated_data = updated_data.replace(':heavy_check_mark:', 'TRUE')  # Replace :heavy-check-mark: with TRUE
                updated_data = updated_data.replace(':heavy_minus_sign:', 'FALSE')  # Replace :heavy-minus-sign: with FALSE
                updated_data = updated_data.replace(
                    r'\[([^\]]+)\]\(\.\.\/\.\.\/models\/([^\)]+)\.md\)',
                    r'[\1](/python-sdk-docs/models/\2)'
                )  # Update links

                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(updated_data)
                print(f"Moved and updated {src_path} to {dest_path}")

def update_mint_json():
    mint_json_path = 'mintlify/mint.json'
    with open(mint_json_path, 'r', encoding='utf-8') as f:
        mint_json = json.load(f)

    models_dir = 'python-sdk-docs/models'
    models_pages = get_markdown_files(models_dir)

    navigation = mint_json.get('navigation', [])

    for nav_item in navigation:
        if nav_item.get('group') == 'Models':
            nav_item['pages'] = models_pages

    with open(mint_json_path, 'w', encoding='utf-8') as f:
        json.dump(mint_json, f, indent=2)
    print('Updated mint.json')

# Example usage
move_and_update_files('docs/sdks/', 'mintlify')
move_and_update_files('docs/models/', 'mintlify')
update_mint_json()
