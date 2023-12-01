import flet
from flet import *

def main(page:Page):
    def miscroll(e:OnScrollEvent):
        print(e)
    body = Column(
        width=page.window_width,
        height=500,
        scroll="always",
        on_scroll_interval=0,
        on_scroll=miscroll
    )
    for x in range(0,20):
        body.controls.append(
            Container(
                bgcolor="white",
                border_radius=30,
                margin=margin.only(left=30,right=39),
                content=Text(f"you data -", size=20)
            )
        )
    
    page.add(
        Column([
            Text("Infinity Scroll",weight="bold",size=30),
            Container(
                bgcolor="blue",
                padding=10,
                content=body
            )
        ])
    )
flet.app(target=main)