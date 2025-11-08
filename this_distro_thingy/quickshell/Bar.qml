import Quickshell
import Quickshell.Io
import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Shapes

Scope {
    id: root
    property string time

    Variants {
        model: Quickshell.screens;

        PanelWindow {
            id: toplevel
            required property var modelData
            screen: modelData

            color: "transparent"

            anchors {
                top: true
                left: true
                right: true
            }

            implicitHeight: 50

            Rectangle {
                anchors {
                    fill: parent
                    leftMargin: 10
                    rightMargin: 10
                    topMargin: 10
                    bottomMargin: 0
                }
                color: "pink"
                bottomLeftRadius: 20
                bottomRightRadius: 20
                topLeftRadius: 20
                topRightRadius: 20

                Item {
                    anchors.centerIn: parent
                    width: 230
                    height: 42
                    Button {
                        id: clockButton
                        text: root.time 
                        anchors {
                            fill: parent
                            margins: 8
                        }
                        onClicked: clockPopup.visible = !clockPopup.visible
                        background: Rectangle {
                            bottomLeftRadius: 20
                            bottomRightRadius: 20
                            topLeftRadius: 20
                            topRightRadius: 20
                            color: parent.down ? "#bbbbbb" :
                                parent.hovered ? "#d6d6d6" : "#f6f6f6"
                        }
                    }
                }
            }
            PopupWindow {
                id: clockPopup
                anchor.window: toplevel
                anchor.rect.x: parentWindow.width / 2 -width / 2
                anchor.rect.y: parentWindow.height
                implicitWidth: 500
                implicitHeight: 500
                visible: false
                color: "transparent"
                Rectangle {
                    color: "pink"
                    anchors {
                        fill: parent
                        topMargin: 10
                    }
                    radius: 20
                    Text {
                        text: "The time is.... jk im not telling u\n ok here you go: " + root.time + "\n dunno why you clicked on this just to see the time again but oh well..."
                        anchors.centerIn: parent
                    }
                }
            }
        }
    }

    Process {
        id: dateProc
        command: ["date"]
        running: true

        stdout: StdioCollector {
            onStreamFinished: root.time = this.text
        }
    }

    Timer {
        interval: 1000
        running: true
        repeat: true
        onTriggered: dateProc.running = true
    }
}