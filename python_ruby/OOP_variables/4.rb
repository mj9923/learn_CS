class C
  attr_reader :value
  attr_writer :value
  attr_accessor :value
  def initialize(v)
    @value = v
  end
  def show()
    p @vlue
  end
  def getValue()
    return @value
  end
  def setValue(v)
    @value = v
  end
end

c1 = C.new(10)
p c1.value
c1.value = 20
p c1.value
