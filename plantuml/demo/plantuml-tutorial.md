[TOC]

## sequece diagram

```plantuml
@startuml
title basic example
A -> B: Hi
A <-- B: "Hi, how are you? long time no see"
@enduml
```

### overview

1. default type is `participant`, `->` and `<--`

2. types
    - actor
    - entity
    - collection
    - database
    - control
    - boundary

> order as they declared

3. alias `as`, color `#rgb`

4. title and note

5. text wrapping, `\n` or skinParameter `maxMessageSize`

### declaring

```plantuml
@startuml
skinparam maxMessageSize 50
title **declaring participants**

participant default
actor A
entity B
collections C
control D
boundary Bound as B2 #00FF00
database DB
actor A2 #red

A -> B : have a realy long name
note left: show me the code

participant "android::ExynosCameraConfiguration" as AB #99FF99
@enduml
```

### arrow styles

1. `->, -->, -\, ->x, ->o, <->`, double for a thin drawing
2. color, `-[#red]>`

```plantuml
@startuml
title arrows
Bob ->x Alice
Bob -[#black]> Alice
Bob ->> Alice
Bob -\ Alice
Bob \\- Alice
Bob //-- Alice
Bob ->o Alice
Bob o\\-- Alice
Bob <-> Alice
Bob <->o Alice
@enduml
```

### message sequece autonumber

- `autonumber start increment "msg foramt 0"`, 0 is the number

```plantuml
@startuml
autonumber 10 10 "<b>[000]"
Bob -> Alice : Authentication Request
Bob <- Alice : Authentication Response

autonumber stop
Bob -> Alice : dummy

autonumber resume "<font color=red><b>Message 0  "
Bob -> Alice : Yet another authentication Request
Bob <- Alice : Yet another authentication Response

autonumber stop
Bob -> Alice : dummy

autonumber resume 1 "<font color=blue><b>Message 0  "
Bob -> Alice : Yet another authentication Request
Bob <- Alice : Yet another authentication Response
@enduml
```

### page title, header and footer

```plantuml
@startuml
header show on every page
footer each, %page% of %lastpage%

title message Q
actor A
actor B
A <-> B : MQ1

newpage page2

A -> B : requests
A <-- B : responses

@enduml
```

### grouping messages

1. keywords
   - alt/else
   - opt
   - loop
   - group

2. `end`

```plantuml
@startuml
A -> B: request

alt ok
A <-- B: successful
else fail
A <-- B: failed, due to xxx
end

opt failed
    A -> B: attack start
    loop 1000 times
        A -> B: DNS attack
        opt success
            A <-- B: log in
            A -> B: attack end
        end
    end
    A -> B: attack end
end

group important [must]
A -> B: clear self's trace info
end
note right: important

@enduml
```

### notes on message

1. `note left` or `note right`, related to **arrow**
2. multiple line notes, using `end note`

3. `left of, right of, over`, related to **participant**, color applied

```plantuml
@startuml
participant A #yellow
A -> B: hello
note left #red: first
note right: nice buddy

A -> B: show me the code
note right
Talk is cheap, show me the
code. --Linux
end note

group talk between A & B
    note over A #FFAAAA: something else?
    note over A #FFAAAA: something else???
    note over B: no, i'm sorry about it
end
@enduml
```

### markdown and HTML

leagcy HTML

```
<b> for bold text
<u> or <u:#AAAAAA> or <u:[[color|colorName]]> for underline
<i> for italic
<s> or <s:#AAAAAA> or <s:[[color|colorName]]> for strike text
<w> or <w:#AAAAAA> or <w:[[color|colorName]]> for wave underline text
<color:#AAAAAA> or <color:[[color|colorName]]>
<back:#AAAAAA> or <back:[[color|colorName]]> for background color
<size:nn> to change font size
<img:file> : the file must be accessible by the filesystem
<img:http://plantuml.com/logo3.png> : the URL must be available from the Internet
```

```plantuml
@startuml
Alice -> Bob : hello --there--
... Some ~~long delay~~ ...
Bob -> Alice : ok
note left
This is **bold**
This is //italics//
This is ""monospaced""
This is --stroked--
This is __underlined__
This is ~~waved~~
end note

Alice -> Bob : A //well formatted// message
note right of Alice
This is <back:reverse><size:18>displayed</size></back>
__left of__ Alice.
end note

note left of Bob
<u:red>This</u> is <color #118888>displayed</color>
**<color purple>left of</color> <s:red>Alice</strike> Bob**.
end note
note over Alice, Bob
<w:#FF33FF>This is hosted</w> by <img images/plantuml/seq-pages/message Q.png>
end note
@enduml
```

### divides, delay

1. `==, ...`

```plantuml
@startuml
participant ExynosCamera as A
participant ExynosCameraPlugin as B

...

A -> B: connectPPScenario(scenario)
==init==

note over A: TODO
==setup==

note over A: TODO
==process==

... <color:red>device_flsuh ...
note over A: TODO
==deinit==

@enduml
```

### lifetime activate and Destruction

1. `activate`, `deactive`, `create`, `destroy`, `return`

```plantuml
@startuml
participant User
User -> A: Dowork
activate A
A -> B: << create request>>
activate B
B -> B: createRequest
activate B #99FF99
create C
B -> C: new
activate C
C -> C: dowork
return: workdone
destroy C
deactivate B
B --> A: << request done>>
deactivate B
A --> User: done
deactivate A
@enduml
```

2. `++, --, **, !!`, activate, deactivate, create and destroy
3. The return point is that which caused the most recent life-line activation.

```plantuml
@startuml
participant alice
participant bob
participant bill
alice -> bob: Hello
activate bob
bob -> bob: something self
activate bob
bill -> bob: waits hello from thread2
activate bob #green
bob -> george ** : create
bob --> bill: done in thread2
deactivate bob
return ret
bob -> george !! : delete
bob --> alice: succesful
deactivate bob
@enduml
```

```plantuml
@startuml
alice -> bob++: hello
bob -> bob++: something self
bill -> bob++ #green: waits hello from bill
bob -> george **: new
bob --> bill--: done for bill
return ret
bob -> george !!: delete
bob --> alice: successful
@enduml
```

### incoming and outgoing messages

1. `[, ]`

```plantuml
@startuml
[-> HAL ++: proceessRequest
HAL ->] ++: push req to requestWaitingList, start mainPreviewThread
return ret
return ret
@enduml
```

### anchors and duration

1. `{A}, {B}`
```plantuml

@startuml
!pragma teoz true

alice -> bob++: hello
bob -> bob++: something self
{A} bill -> bob++ #green: waits hello from bill
bob -> george **: new
{B} bob --> bill--: done for bill
{A} <-> {B} : timeout 100ms
return ret
bob -> george !!: delete
bob --> alice: successful

@enduml
```

### participants encompass

1. `box`, `end box`

```plantuml
@startuml
box "Internal Service" #LightBlue
participant Bob
participant Alice
end box
participant Other
Bob -> Alice : hello
Alice -> Other : hello
@enduml
```

## use case

### basic

```plantuml
@startuml
(3AA)
@enduml
```

## Activity

### basic

1. `start` and `end`
2. `:activity;`
3. condition

```
if (A) then lableA
 activity1
else labelB
 activity2
endif
```

```plantuml
@startuml
' !pragma useVerticalIf on
start
:hello plantuml activity;
:activity cross **multiple**
lines;

if (condition A) then (yes)
    :process A;
elseif (condition B) then (yes)
    :process B;
    stop
elseif (condition C) then (yes)
    :process C;
else (nothing)
    #lightgreen:pass;
endif

stop
@enduml
```