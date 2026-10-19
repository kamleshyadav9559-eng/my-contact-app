import flet as ft

def main(page: ft.Page):
    page.title = "Contact Book"
    page.theme_mode = ft.ThemeMode.LIGHT

    # मोबाइल स्टोरेज से डेटा लोड करना
    contacts = page.client_storage.get("contacts") or {}

    name_input = ft.TextField(label="नाम (Name)", expand=True)
    phone_input = ft.TextField(label="मोबाइल नंबर (Phone)", keyboard_type=ft.KeyboardType.PHONE, expand=True)
    contact_list = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def update_list():
        contact_list.controls.clear()
        for name, phone in contacts.items():
            contact_list.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(name, weight=ft.FontWeight.BOLD),
                    subtitle=ft.Text(phone),
                    trailing=ft.IconButton(
                        icon=ft.Icons.DELETE,
                        icon_color="red",
                        on_click=lambda e, n=name: delete_contact(n)
                    )
                )
            )
        page.update()

    def add_contact(e):
        name = name_input.value.strip()
        phone = phone_input.value.strip()
        if name and phone:
            contacts[name] = phone
            page.client_storage.set("contacts", contacts)
            name_input.value = ""
            phone_input.value = ""
            update_list()

    def delete_contact(name):
        if name in contacts:
            del contacts[name]
            page.client_storage.set("contacts", contacts)
            update_list()

    add_btn = ft.ElevatedButton(text="कॉन्टैक्ट सेव करें", on_click=add_contact)

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Text("📞 मेरी कॉन्टैक्ट बुक", size=24, weight=ft.FontWeight.BOLD),
                    ft.Row([name_input]),
                    ft.Row([phone_input]),
                    add_btn,
                    ft.Divider(),
                    contact_list
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            ),
            expand=True
        )
    )
    update_list()

ft.app(target=main)
