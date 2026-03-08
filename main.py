import flet as ft
from googletrans import Translator

async def main(page: ft.Page):
    # هذه الإعدادات ستعمل على الكمبيوتر فقط لمعاينة الحجم، ولن تؤثر على الهاتف
    page.window.width = 390
    page.window.height = 844
    page.window.resizable = False
    
    # إبعاد العناصر عن حواف الشاشة ليكون التصميم جميلاً على الهاتف
    page.padding = 20 

    result_text = ft.Text(value="", size=20, color="blue", selectable=True, rtl=True)

    async def translation_event(e):
        if not text_field.value:
            return

        # إيقاف الزر
        the_button.content.disabled = True
        page.update()

        try:
            async with Translator() as translator:
                result = await translator.translate(text=text_field.value, dest="ar")
                result_text.value = result.text
        except Exception as ex:
            result_text.value = f"خطأ في الاتصال بالإنترنت أو الخادم" # رسالة ألطف للمستخدم
            print(ex)

        # إعادة تشغيل الزر
        the_button.content.disabled = False
        page.update()

    the_title = ft.Container(
        content=ft.Text("The Translator", size=30, color=ft.Colors.GREEN, weight=ft.FontWeight.BOLD),
        alignment=ft.Alignment.CENTER,
    )

    result = ft.Container(
        content=result_text, 
        alignment=ft.Alignment.CENTER_RIGHT
    )

    text_field = ft.TextField(
        label="Enter Text To Translate",
        text_size=20,
        border_radius=20,
        border_color="green",
        multiline=True,
        min_lines=3, 
        max_lines=7, 
        expand=True
    )

    the_button = ft.Container(
        # 🌟 تم تصحيح ft.Button إلى ft.ElevatedButton
        content=ft.Button(
            content=ft.Text(value="Translate", size=20),
            on_click=translation_event,
            height=50,
        ),
        alignment=ft.Alignment.CENTER,
    )

    my_elements = ft.Column(
        controls=[the_title, text_field, the_button, result], 
        spacing=30,
        # هذه الخاصية تضمن أن العناصر لا تتجاوز الشاشة (تضيف سكرول إذا امتلأت الشاشة)
        scroll=ft.ScrollMode.AUTO 
    )

    page.add(my_elements)

ft.app(target=main)