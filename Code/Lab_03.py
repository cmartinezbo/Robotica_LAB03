from robodk.robolink import *    # API para comunicarte con RoboDK
from robodk.robomath import *    # Funciones matemáticas
import math

#------------------------------------------------
# 1) Conexión a RoboDK e inicialización
#------------------------------------------------

RDK = Robolink()

# Elegir un robot (si hay varios, aparece un popup)
robot = RDK.ItemUserPick("Selecciona un robot", ITEM_TYPE_ROBOT)
#if not robot.Valid():
 #   raise Exception("No se ha seleccionado un robot válido.")

# Conectar al robot físico
#if not robot.Connect():
#    raise Exception("No se pudo conectar al robot. Verifica que esté en modo remoto y que la configuración sea correcta.")

# Confirmar conexión
#if not robot.ConnectedState():
 #   ("El robot no está conectado correctamente. Revisa la conexión.")

print("Robot conectado correctamente.")

#------------------------------------------------
# 2) Cargar el Frame
#------------------------------------------------
frame_name2 = "HOME"
frame2 = RDK.Item(frame_name2, ITEM_TYPE_FRAME)
if not frame2.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name2}" en la estación.')

robot.setPoseFrame(frame2)
robot.setPoseTool(robot.PoseTool())

# Ajustes de velocidad y blending
robot.setSpeed(300)   # mm/s
robot.setRounding(5)  # mm

robot.MoveJ(transl(0, 0, 0))


frame_name = "Frame_from_Target1"
frame = RDK.Item(frame_name, ITEM_TYPE_FRAME)
if not frame.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name}" en la estación.')

robot.setPoseFrame(frame)
robot.setPoseTool(robot.PoseTool())

# Ajustes de velocidad y blending
robot.setSpeed(300)   # mm/s
robot.setRounding(5)  # mm

#------------------------------------------------
# 3) Parámetros del cuarto de círculo
#------------------------------------------------
num_points = 180
radius = 150
z_surface = 0
z_safe = -50

# Offset para mover el centro del círculo
offset_x = 0
offset_y = 300*math.sin(math.pi/4)
last_y = 0
last_x = 0
last_y2 = 0
last_x2 = 0
#------------------------------------------------
# 4) Ir al punto inicial en altura segura
#------------------------------------------------
robot.MoveJ(transl(0, 0, z_surface + z_safe))
robot.MoveL(transl(0, 0, z_surface))  # punto inicial desplazado

#------------------------------------------------
# 5) Dibujar un cuarto de círculo (0° a 45°), centrado en (10, 0)
#------------------------------------------------
start_angle = 7*math.pi / 4
end_angle = 9*math.pi / 4

for i in range(num_points + 1):
    t = i / num_points
    theta = start_angle + (end_angle - start_angle) * t

    x = radius * math.cos(theta)
    y = radius * math.sin(theta)

    robot.MoveL(transl(x, y, z_surface))

start_angle = 7*math.pi / 4
end_angle = 9*math.pi / 4

for i in range(num_points + 1):
    t = i / num_points
    theta = start_angle + (end_angle - start_angle) * t

    x = offset_x + radius * math.cos(theta)
    y = offset_y + radius * math.sin(theta)

    robot.MoveL(transl(x, y, z_surface))

robot.MoveL(transl(160, 375, z_surface))

start_angle = 7*math.pi / 6
end_angle = 7*math.pi / 4

for i in range(num_points + 1):
    t = i / num_points
    theta = start_angle + (end_angle - start_angle) * t

    x = 300 + radius * math.cos(theta)
    y = 450 + radius * math.sin(theta)
    last_x = x
    last_y = y

    robot.MoveL(transl(x, y, z_surface))

start_angle = math.pi / 2
end_angle = 0

for i in range(num_points + 1):
    t = i / num_points
    theta = start_angle + (end_angle - start_angle) * t

    x = last_x + radius * math.cos(theta)
    y = last_y - 150 + radius * math.sin(theta)
    last_x2 = x
    last_y2 = y

    robot.MoveL(transl(x, y, z_surface))

start_angle = math.pi
end_angle = 7*math.pi / 6

for i in range(num_points + 1):
    t = i / num_points
    theta = start_angle + (end_angle - start_angle) * t

    x = last_x2 + 150 + radius * math.cos(theta)
    y = last_y2 + radius * math.sin(theta)
    last_x = x
    last_y = y

    robot.MoveL(transl(x, y, z_surface))

robot.MoveL(transl(580, 150*math.sin(math.pi/4), z_surface))
robot.MoveL(transl(last_x, 150*math.sin(math.pi/4)-
                   (last_y-150*math.sin(math.pi/4)), z_surface))

end_angle = math.pi
start_angle = 5*math.pi / 6

for i in range(num_points + 1):
    t = i / num_points
    theta = start_angle + (end_angle - start_angle) * t

    x = last_x + 150*math.cos(math.pi/6) + radius * math.cos(theta)
    y = 150*math.sin(math.pi/4)-(last_y-150*math.sin(math.pi/4)) - 150*math.sin(math.pi/6) + radius * math.sin(theta)
    last_x2 = x
    last_y2 = y

    robot.MoveL(transl(x, y, z_surface))

end_angle = 3*math.pi / 2
start_angle = 2*math.pi

for i in range(num_points + 1):
    t = i / num_points
    theta = start_angle + (end_angle - start_angle) * t

    x = last_x2 - 150 + radius * math.cos(theta)
    y = last_y2 + radius * math.sin(theta)
    last_x = x
    last_y = y

    robot.MoveL(transl(x, y, z_surface))

end_angle = 5*math.pi / 6
start_angle = math.pi / 4

for i in range(num_points + 1):
    t = i / num_points
    theta = start_angle + (end_angle - start_angle) * t

    x =  last_x - 150*math.sin(math.pi/4) + radius * math.cos(theta)
    y =  last_y - 150*math.sin(math.pi/4) + radius * math.sin(theta)
    last_x2 = x
    last_y2 = y

    robot.MoveL(transl(x, y, z_surface))

robot.MoveL(transl(160, last_y2, z_surface))
robot.MoveL(transl(radius * math.cos(7*math.pi / 4), radius * math.sin(7*math.pi / 4), z_surface))

#------------------------------------------------
# 6) Altura segura final
#------------------------------------------------
robot.MoveL(transl(x, y, z_surface + z_safe))

print(f"¡Cuarto de círculo centrado en (X=10, Y=0) completado en el frame '{frame_name}'!")

frame_name2 = "HOME"
frame2 = RDK.Item(frame_name2, ITEM_TYPE_FRAME)
if not frame2.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name2}" en la estación.')

robot.setPoseFrame(frame2)
robot.setPoseTool(robot.PoseTool())

# Ajustes de velocidad y blending
robot.setSpeed(300)   # mm/s
robot.setRounding(5)  # mm

robot.MoveJ(transl(0, 0, 0))
