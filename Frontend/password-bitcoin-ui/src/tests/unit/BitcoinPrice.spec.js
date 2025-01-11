import { mount } from "@vue/test-utils";
import BitcoinPrice from "@/components/BitcoinPrice.vue";

describe("BitcoinPrice.vue", () => {
  it("renders button", () => {
    const wrapper = mount(BitcoinPrice);
    expect(wrapper.find("button").exists()).toBe(true);
  });

  it("fetches bitcoin price on button click", async () => {
    const wrapper = mount(BitcoinPrice);
    await wrapper.find("button").trigger("click");
    // Mock API call or check if price is fetched
    expect(wrapper.vm.bitcoinPrice).toBeTruthy();
  });
});
