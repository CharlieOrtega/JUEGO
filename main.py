from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from game.board import Board
from kivy.uix.boxlayout import BoxLayout


class PlayerInfo(BoxLayout):
    def __init__(self, player1, player2, **kwargs):
        super(PlayerInfo, self).__init__(**kwargs)
        self.orientation = 'horizontal'

        # Widget para mostrar información del jugador 1
        player1_info = BoxLayout(orientation='vertical')
        player1_label = Label(text=f'Jugador 1\nPiezas restantes: {len(player1.hand)}')
        player1_info.add_widget(player1_label)

        # Widget para mostrar información del jugador 2
        player2_info = BoxLayout(orientation='vertical')
        player2_label = Label(text=f'Jugador 2\nPiezas restantes: {len(player2.hand)}')
        player2_info.add_widget(player2_label)

        # Agregar widgets al layout principal
        self.add_widget(player1_info)
        self.add_widget(player2_info)


class GameBoard(GridLayout):
    def __init__(self, **kwargs):
        super(GameBoard, self).__init__(**kwargs)
        self.cols = 7
        self.rows = 6
        self.board = Board(self.rows, self.cols)

        for i in range(self.rows * self.cols):
            btn = Button(text='', font_size=14)
            btn.bind(on_release=self.on_button_release)
            if (i // self.cols + i % self.cols) % 2 == 0:
                btn.background_color = (0.3, 0.3, 0.3, 1)
            else:
                btn.background_color = (0.8, 0.8, 0.8, 1)
            self.add_widget(btn)

    def on_button_release(self, instance):
        row, col = self.get_button_position(instance)
        if instance.text == '':
            instance.text = 'X'
            self.board.place_piece(row, col, 'X')
        else:
            instance.text = ''
            self.board.place_piece(row, col, None)

    def get_button_position(self, button):
        index = self.children.index(button)
        row = index // self.cols
        col = index % self.cols
        return row, col


class BatallaApp(App):
    def build(self):
        # Crear instancia de la clase PlayerInfo con ambos jugadores
        player_info = PlayerInfo(player1, player2)

        # Crear instancia de la clase GameBoard
        game_board = GameBoard()

        # Crear layout principal y agregar widgets
        root = BoxLayout(orientation='vertical')
        root.add_widget(player_info)
        root.add_widget(game_board)

        return root

if __name__ == "__main__":
    BatallaApp().run()
