// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "SupremeSetuHubIOS",
    platforms: [.iOS(.v16)],
    products: [
        .library(name: "SupremeSetuHubIOS", targets: ["SupremeSetuHubIOS"])
    ],
    targets: [
        .target(name: "SupremeSetuHubIOS", path: "Sources/SupremeSetuHubIOS")
    ]
)
