import os


def pack_project():
    current_dir = os.getcwd()
    project_name = os.path.basename(current_dir)
    output_file = f"contexto_{project_name}.txt"

    code_extensions = ('.py', '.c', '.h', '.js', '.html', '.css', '.json', '.md')
    ignore_list = {'.git', '.github', '.venv', '__pycache__', 'node_modules'}

    total_chars = 0
    count = 0

    with open(output_file, "w", encoding="utf-8") as f_out:
        for root, dirs, files in os.walk(current_dir):
            dirs[:] = [d for d in dirs if d not in ignore_list and not d.startswith('.')]
            for file in files:
                if file.endswith(code_extensions) and file != output_file:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, current_dir)

                    f_out.write(f"\n\n{'=' * 60}\n### ARCHIVO: {rel_path}\n{'=' * 60}\n\n")

                    try:
                        with open(full_path, "r", encoding="utf-8", errors="ignore") as f_in:
                            contenido = f_in.read()
                            f_out.write(contenido)
                            total_chars += len(contenido)
                        count += 1
                    except Exception as e:
                        f_out.write(f"[ERROR: {e}]\n")

    # Estimación de tokens (aprox. 4 caracteres por token en código)
    tokens_est = total_chars // 4

    print(f"✅ Proyecto '{project_name}' empaquetado.")
    print(f"📄 Archivos procesados: {count}")
    print(f"📊 Tamaño estimado: {tokens_est:,} tokens.")
    print(f"💡 (Límite NotebookLM: 500,000 por archivo)")


if __name__ == "__main__":
    pack_project()