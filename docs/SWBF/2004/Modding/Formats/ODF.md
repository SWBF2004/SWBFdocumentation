# ODF (Object Definition File)


Example (bes1_bldg_gas_cell.odf):
```odf
[GameObjectClass]

ClassLabel    =  "prop"
GeometryName  =  "bes1_bldg_gas_cell.msh"


[Properties]

GeometryName  =  "bes1_bldg_gas_cell"

FoleyFXGroup  = "metal_foley"
```


## Section
| Value              | Description |
| :----------------- | :---------- |
| GameObjectClass    |             |
| ExplosionClass     |             |
| OrdnanceClass      |             |
| WeaponClass        |             |
| Properties         |             |
| InstanceProperties |             |

### GameObjectClass
| Parameter     | Description |
| :------------ | :---------- |
| ClassLabel    |             |
| GeometryName  |             |
| GeometryScale |             |

### ExplosionClass
| Parameter  | Value(s)  | Description |
| :--------- | :-------- | :---------- |
| ClassLabel | explosion |             |

### WeaponClass
| Parameter       | Value(s) | Description |
| :-------------- | :------- | :---------- |
| AnimationBank   |          |             |
| HighResGeometry |          |             |

### ClassLabel
| Value                        | Description |
| :--------------------------- | :---------- |
| animatedbuilding             |             |
| animatedprop                 |             |
| armedbuilding                |             |
| armedbuildingdynamic         |             |
| asteroid                     |             |
| beacon                       |             |
| beam                         |             |
| binoculars                   |             |
| bldg                         |             |
| bolt                         |             |
| building                     |             |
| bullet                       |             |
| cannon                       |             |
| catapult                     |             |
| cloth                        |             |
| cloudcluster                 |             |
| commandarmedanimatedbuilding |             |
| commandhover                 |             |
| commandpost                  |             |
| commandhover                 |             |
| commandwalker                |             |
| destruct                     |             |
| destructablebuilding         |             |
| detonator                    |             |
| disguise                     |             |
| dispenser                    |             |
| door                         |             |
| droid                        |             |
| dusteffect                   |             |
| emitterordnance              |             |
| explosion                    |             |
| fatray                       |             |
| flag                         |             |
| flyer                        |             |
| godray                       |             |
| grapplinghook                |             |
| grapplinghookweapon          |             |
| grasspatch                   |             |
| grenade                      |             |
| haywire                      |             |
| hologram                     |             |
| hover                        |             |
| launcher                     |             |
| leafpatch                    |             |
| Light                        |             |
| melee                        |             |
| mine                         |             |
| missle                       |             |
| powerupitem                  |             |
| powerupstation               |             |
| prop                         |             |
| remote                       |             |
| repair                       |             |
| rumbleeffect                 |             |
| shell                        |             |
| shield                       |             |
| soldier                      |             |
| SoundAmbienceStatic          |             |
| SoundAmbienceStreaming       |             |
| sticky                       |             |
| towcable                     |             |
| towcableweapon               |             |
| trap                         |             |
| vehiclepad                   |             |
| vehiclespawn                 |             |
| walker                       |             |
| walkerdroid                  |             |
| water                        |             |
| weapon                       |             |

### Properties
| Key               | Value                | Description |
| :---------------- | :------------------- | :---------- |
| BUILDINGSECTION   | BODY                 |             |
| Label             | `[label: string]`    |             |
| CaptureTime       | `[time: float]`      |             |
| NeutralizeTime    | `[time: float]`      |             |
| MapTexture        | `[texture: string]`  |             |
| MapScale          | `[scale: float]`     |             |
| HoloOdf           | `[odf: string]`      |             |
| HoloImageGeometry | `[geometry: string]` |             |
| HoloTurnOnTime    | `[time: float]`      |             |
| Lighting          | `["dynamic", ...]`   |             |