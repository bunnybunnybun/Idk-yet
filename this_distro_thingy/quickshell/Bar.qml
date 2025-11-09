import Quickshell
import Quickshell.Io
import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

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
                    leftMargin: 20
                    rightMargin: 20
                    topMargin: 10
                    bottomMargin: 0
                }
                color: Qt.rgba(1, 0, 0.788, 0.6)
                bottomLeftRadius: 20
                bottomRightRadius: 20
                topLeftRadius: 20
                topRightRadius: 20
                border.color: Qt.rgba(1.0, 0.7, 0.988, 1.0)
                border.width: 3

                RowLayout {
                    anchors.fill: parent
                    RowLayout {
                        id: leftModules
                        anchors.fill: parent
                        spacing: 10

                        Button {
                            id: clockButton
                            text: root.time
                            Layout.preferredHeight: 25
                            Layout.preferredWidth: 230
                            onClicked: clockPopup.visible = !clockPopup.visible
                            background: Rectangle {
                                bottomLeftRadius: 20
                                bottomRightRadius: 20
                                topLeftRadius: 20
                                topRightRadius: 20
                                color: parent.down ? Qt.rgba(1.0, 0.7, 0.988, 1.0) :
                                    parent.hovered ? Qt.rgba(1.0, 0.85, 1.0, 1.0) : Qt.rgba(1.0, 0.7, 0.988, 1.0)
                            }
                        }

                        
                    }

                    //Item {
                    //    Layout.fillWidth: true
                    //}

                    RowLayout {
                        id: rightModules
                        Layout.alignment: Qt.AlignRight
                        Layout.fillWidth: true

                        Button {
                            id: trayButton
                            contentItem: Label {
                                text: "󰁋"
                                font.pixelSize: 18
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                            }
                            //Layout.alignment: Qt.AlignRight
                            anchors.rightMargin: 8
                            Layout.preferredHeight: 25
                            Layout.preferredWidth: 50
                            onClicked: trayPopup.visible = !trayPopup.visible
                            background: Rectangle {
                                bottomLeftRadius: 20
                                bottomRightRadius: 20
                                topLeftRadius: 20
                                topRightRadius: 20
                                color: parent.down ? Qt.rgba(1.0, 0.7, 0.988, 1.0) :
                                    parent.hovered ? Qt.rgba(1.0, 0.85, 1.0, 1.0) : Qt.rgba(1.0, 0.7, 0.988, 1.0)
                            }
                        }

                        Button {
                            id: settingsButton
                            contentItem: Label {
                                text: "󰁋"
                                font.pixelSize: 18
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                            }
                            Layout.preferredHeight: 25
                            Layout.preferredWidth: 50
                            onClicked: trayPopup.visible = !trayPopup.visible
                            background: Rectangle {
                                bottomLeftRadius: 20
                                bottomRightRadius: 20
                                topLeftRadius: 20
                                topRightRadius: 20
                                color: parent.down ? Qt.rgba(1.0, 0.7, 0.988, 1.0) :
                                    parent.hovered ? Qt.rgba(1.0, 0.85, 1.0, 1.0) : Qt.rgba(1.0, 0.7, 0.988, 1.0)
                            }
                        }
                    }
                }
            }

            PopupWindow {
                id: clockPopup
                anchor.window: toplevel
                anchor.rect.x: parentWindow.width / 2 -width / 2
                anchor.rect.y: 50
                implicitWidth: 500
                implicitHeight: 500
                visible: false
                color: "transparent"
                Rectangle {
                    color: Qt.rgba(1.0, 0.0, 0.788, 0.8)
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

            PopupWindow {
                id: trayPopup
                anchor.item: trayButton
                anchor.gravity: Edges.Bottom | Edges.Left
                anchor.rect.y: 32
                anchor.rect.x: 58
                implicitWidth: 300
                implicitHeight: 500
                visible: false
                color: "transparent"
                Rectangle {
                    color: Qt.rgba(1.0, 0.0, 0.788, 0.8)
                    anchors {
                        fill: parent
                        topMargin: 10
                    }
                    radius: 20
                    Text {
                        text: "Tray thingy"
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