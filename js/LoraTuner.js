import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "LoraTuner",
    nodeCreated(node) {
        if ((node.type, node.constructor.comfyClass !== "LoraTuner")) return;
        node.widgets.forEach(w => {
            if (w.type === "slider") {
                w.computeSize = () => [0, LiteGraph.NODE_WIDGET_HEIGHT * 1.5]; // for margin
            }
        });
    }
})
