# MSH (Mesh)

## Mesh nodes
| Element                      | Meaning            | Description                                                         |
| :--------------------------- | :----------------- | :------------------------------------------------------------------ |
| `collision_[]`               | Collision geometry | Separate mesh for collision (usually not visible).                  |
| `hp_[]`                      | Hard point         | Used to attach other objects or for interaction.                    |
| `terraincutter_[cube , ...]` | Terrain cutter     | Used to cut a hole with the dimension of the mesh into the terrain. |
| `sv_[]`                      | Shadow Volume      | Used for rendering shadows of the mesh.                             |
