import pygame, sys
from game import Game

pygame.init()
DARK = (26, 24, 24)
# wyświetlanie inputów dla użytkownika wraz z walidacją
def get_user_input(prompt, min_val, max_val):
    while True:
        user_input = input(f"{prompt} ({min_val}-{max_val}): ")
        try:
            value = int(user_input)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Wartość musi się znajdować pomiędzy {min_val} a  {max_val}.")
        except ValueError:
            print("Prosze podać poprawną liczbę.")

# główna funkcja
def main():
    font = pygame.font.SysFont('Arial', 20, bold=True)
    print("Wybierz jedną z opcji:")
    print("1) Użyj domyślnych wartości")
    print("2) Wprowadź własne parametry")
    choice = input("Wpisz 1 albo 2: ")

    if choice == "1":
        WINDOW_WIDTH = 800
        WINDOW_HEIGHT = 800
        CELL_SIZE = 20
        FPS = 6
    elif choice == "2":
        WINDOW_WIDTH = get_user_input("Podaj szerokość okna: ", 700, 1400)
        WINDOW_HEIGHT = get_user_input("Podaj wysokość okna: ", 500, 900)
        CELL_SIZE = get_user_input("Podaj rozmiar komórki: ", 4, 24)
        FPS = get_user_input("Podaj liczbę generacji na sekundę: ", 5, 20)
    else:
        print("Nieprawidłowy wybór, wybrano opcję 1.")
        WINDOW_WIDTH = 800
        WINDOW_HEIGHT = 800
        CELL_SIZE = 20
        FPS = 6


    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Gra jest wstrzymana, naciśnij Enter aby uruchomić")
    clock = pygame.time.Clock()
    sim = Game(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

    while True:
        # obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sim.start()
                    pygame.display.set_caption("Gra jest uruchomiona, naciśnij Spację aby zatrzymać")
                elif event.key == pygame.K_SPACE:
                    sim.stop()
                    pygame.display.set_caption("Gra została zatrzymana, naciśnij Enter aby grać dalej ")
                elif event.key == pygame.K_r:
                    sim.create_random_state()
                elif event.key == pygame.K_c:
                    sim.clear()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not sim.is_running():
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    row = mouse_y // sim.grid.cell_size
                    column = mouse_x // sim.grid.cell_size
                    sim.toggle_cell(row, column)

        sim.update()

        window.fill(DARK)
        sim.draw(window)

        generation_text = font.render(f"Generacja: {sim.generation_count}", True, (255, 255, 255))
        window.blit(generation_text, (10, 10))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
