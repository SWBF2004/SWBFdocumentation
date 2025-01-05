# REQ (Requirement)

The REQ format is a textual format which defines what data is munged into a binary LVL file.
It consists of a number of REQN blocks that specify the type of the data, configuration properties, and the dependant files that belong to that type.

## Data Types

| Type     | Description                                                                 |
| :------- | :-------------------------------------------------------------------------- |
| bnk      | Sound effect files like *.sfx.                                              |
| boundary |                                                                             |
| class    |                                                                             |
| config   | Sound effect and music stream configuration files like *.ffx, *.mus, *.snd. |
| congraph |                                                                             |
| envfx    |                                                                             |
| loc      |                                                                             |
| lvl      |                                                                             |
| model    |                                                                             |
| path     |                                                                             |
| prop     |                                                                             |
| script   |                                                                             |
| str      | Music stream files like *.st4 or *.stm.                                     |
| terrain  |                                                                             |
| texture  |                                                                             |
| world    |                                                                             |
| zaabin   |                                                                             |
| zafbin   |                                                                             |

## Configuration Properties

| Type     | Description |
| :------- | :---------- |
| align    |             |
| platform |             |

Example (bes1.req):
```req
ucft
{

  REQN
  {
    "zafbin"
  }

  REQN
  {
    "zaabin"
  }

  REQN
  {
    "class"
    "bes_fly_cloudcar"
  }

  REQN
  {
    "texture"
    "bes1_map"
    -- "bird"
  }
  REQN
  {
    "texture"
    "platform=ps2"
  }

  REQN
  {
    "path"
    "bes1"
  }

  REQN
  {
    "congraph"
    "bes1"
  }

  REQN
  {
    "envfx"
    "bes1"
  }

  REQN
  {
    "world"
    "bes1"
  }

  REQN
  {
    "prop"
    "bes1"
  }

  REQN
  {
    "class"
    "bluelight"
    "redlight"
    "greenlight"
    "whitelight"
  }

  REQN
  {
    "boundary"
    "bes1"
  }

  REQN
  {
    "config"
    "flyerspray"
    "walkerstomp"
    "hailfire_wake"
  }

}
```