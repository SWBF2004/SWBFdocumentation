# Console

## SPTest

## Console Commands

### `aimode` (`/ai`)
| Arguments | Description          |
| :-------- | :------------------- |
| `1`       | Enables the ai mode. |

### `ai.aimaxflyheight`
| Arguments           | Description                   |
| :------------------ | :---------------------------- |
| `[height: integer]` | Sets the maximum flyer height. |

### `ai.showobstacles`
| Arguments | Description                                           |
| :-------- | :---------------------------------------------------- |
| `1`       | Enables rendering of barriers (green and blue boxes). |

### `ai.notext` (`/ainotext`)
| Arguments | Description                                |
| :-------- | :----------------------------------------- |
| `1`       | Disables rendering of AI unit information. |

### `ai.showallpaths`
| Arguments | Description                                     |
| :-------- | :---------------------------------------------- |
| `1`       | Enables rendering of AI unit paths (red lines). |

### `ai.showconnectivitygraph`
| Arguments | Description                                                           |
| :-------- | :-------------------------------------------------------------------- |
| `1`       | Enables rendering of the connectivity graph (yellow cylinders lines). |

### `pathcost`
| Arguments | Description                                                               |
| :-------- | :------------------------------------------------------------------------ |
| -         | Disables the pathcost display                                             |
| `ave`     | The average time taken to calculate the connection once.                  |
| `cnt`     | The number of times the connection has been requested.                    |
| `conn`    | The name of the connection in the editor (C16 may resemble Connection16). |
| `max`     | The maximum time taken for one calculation.                               |
| `tot`     | The relative time spent to calculate this connection (in %).              |

### `showflyerheights`
| Arguments | Description                                               |
| :-------- | :-------------------------------------------------------- |
| -         | Enables rendering of the maximum fly height (white grid). |
