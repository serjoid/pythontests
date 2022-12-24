import flet as ft


def main(page: ft.Page):
    page.title = "Formulário de Cadastro"

    nome = ft.TextField(label="Nome:")
    telefone = ft.TextField(label="Telefone:")
    email = ft.TextField(label="Email:")
    endereço = ft.TextField(label="Endereço:")
    dados = ft.Column()

    def btn_click(e):
        dados.controls.append(ft.Text('Dados Gravados com Sucesso!'))

        with open("cadastros.txt", "a") as funcionario:
            funcionario.write(
                f"Nome: {nome.value}, Telefone: {telefone.value}, Email: {email.value}, Endereço: {endereço.value},\n")
        page.update()

    page.add(
        nome,
        telefone,
        email,
        endereço,
        ft.ElevatedButton("Gravar", on_click=btn_click),
        dados,

    )


ft.app(target=main)
