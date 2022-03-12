
import pygame, sys, time, random

pygame.init() # INICIAMOS LA LIBRERIA PYGAME


play_surface = pygame.display.set_mode((500,500)) # DECLARAMOS LA VENTANA DEL JUEGO


font = pygame.font.Font(None, 30) # DECLARAMOS LA VARIABLE DE LAS LETRAS DE SCORE
font_lose = pygame.font.Font(None, 50)

fps = pygame.time.Clock() # DECLARAMOS LOS FPS DEL JUEGO



# FUNCION DE COMIDA
def food():
    random_pos = random.randint(1, 48)*10 # SETEAMOS EL VALOR RANDOM DE LA POSICION DE LA COMIDA
    food_pos = [random_pos, random_pos] # SE LO PASAMOS AÑADIMOS PARA LAS X e Y
    return food_pos


# FUNCION MAIN
def main():
    snake_pos = [100, 50] # POSOCION DE LA SERPIENTE
    snake_body = [[100,50], [90,50], [80,50]] # CUERPO DE LA SERPIENTE
    change = 'RIGHT'
    lose = 'YOU LOSE'
    run = True
    food_pos = food()
    score = 0
    

    # MIENTRAS LA APP ESTE FUNCIONANDO
    while run:
        for event in pygame.event.get(): # COGE EL EVENTO DE LAS TECLAS
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    change = 'LEFT'
                if event.key == pygame.K_UP:
                    change = 'UP'
                if event.key == pygame.K_DOWN:
                    change = 'DOWN'

        # COMPROBAMOS: RESTAMOS O AÑADIMOS PIXELES
        if change == 'RIGHT':
            snake_pos[0] += 10
        if change == 'LEFT':
            snake_pos[0] -= 10
        if change == 'UP':
            snake_pos[1] -= 10
        if change == 'DOWN':
            snake_pos[1] += 10

        snake_body.insert(0, list(snake_pos)) # SE LOS INSERTAMOS EN FORMA DE LISTA

        # SI LA POSICION DE LA CABEZA LA SERPIENTE ES IGUAL A LA POSICION DE LA COMIDA: 
        if snake_pos == food_pos:
            food_pos = food() # VALOR RANDOM A LA COMIDA OTRA VEZ (NUEVA POSICION)
            score += 1 # SUMAMOS LA PUNTUACION
        else:
            snake_body.pop() # SINO VES RESTANDO PIXELES



        play_surface.fill((0,0,0)) # COLOR NEGRO A LA VENTANA

        for pos in snake_body:
            pygame.draw.rect(play_surface, (200, 200, 200), pygame.Rect(pos[0], pos[1], 10, 10)) # AÑADE LA SERPIENTE EN ESTAS POSICIONES POR CADA POSICION DEL CUERPO
        pygame.draw.rect(play_surface, (169, 6, 6), pygame.Rect(food_pos[0], food_pos[1], 10, 10)) # AÑADE LA COMIDA EN LA VENTANA
        text = font.render(str(score), 0, (200, 60, 80)) # RENDERIZAMOS EL COLOR DEL TEXTO
        play_surface.blit(text, (480, 20)) # SE LO AÑADIMOS A LA VENTANA EN ESTAS POSICIONES (480, 20)

        # AUGMENTA LOS FPS A MEDIDA QUE VAMOS SUMANDO PUNTUACION
        if score < 10:
            fps.tick(10)
        if score >= 10 and score < 20:
            fps.tick(20)
        if score >= 20:
            fps.tick(30)

        # ACABA EL JUEGO SI SALIMOS DE LA PANTALLA
        if snake_pos[0] <= 0 or snake_pos[0] >= 500:
            text = font_lose.render(str(lose), 0, (200, 60, 80)) 
            play_surface.blit(text, (200, 250)) 
            pygame.display.flip()
            time.sleep(2)
            run = False

        if snake_pos[1] <= 0 or snake_pos[1] >= 500:
            text = font_lose.render(str(lose), 0, (200, 60, 80)) 
            play_surface.blit(text, (200, 250)) 
            pygame.display.flip()
            time.sleep(2)
            run = False
            
        pygame.display.flip() # ACTUALIZAMOS POR CADA BUCLE WHILE


main() # LLAMAMOS A LA FUNCION MAIN

pygame.quit() # CERRAMOS LA LIBRERIA EN CASO DE SALIR DEL BUCLE