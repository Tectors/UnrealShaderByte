# NOTE: Shaderbyte Materials to Unreal Engine / UEFN

# SHADER PATH FILE - Put the path to the shader path file
shader_path = "FortniteGame/Content/ShaderArchive-FortniteGame-PCD3D_SM5.ushaderbytecode"
material_name = "M_Island_Lake_Master"

# For importing shaders, it is recommended to use the API as it already does everything for you
use_file_import = True
file = {}

Tk().withdraw(); path = askopenfilename(filetypes=[("Shader File", "*")], title='Selection')
print(f'Successfully found {path}')
